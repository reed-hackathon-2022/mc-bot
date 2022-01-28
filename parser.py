from mc import MissedConnection
from sensInfoCheck import *
from download import fetch_document

#
# Helper functions:
# is_int(): Check if the string can be converted to int
# is_MC_start(): Check if the string is the start of MCs file
#

def is_int(element: any):
    try:
        int(element)
        return True
    except ValueError:
        return False


def is_MC_start(string):
    # account for leading whitespace in string
    if string.isspace():    return False
    i = 0
    while string[i].isspace():  i += 1
    while is_int(string[i]):    i += 1
    # must have found integer and have next characters be '.'
    if string[i] == '.' and i != 0:
        return True
    else:                                     return False

def too_long(MC):
    if len(MC) > 280:   return True
    else:               return False

#
# Helper function that takes a MC as a string and returns True if MC is empty
# (this happens if the MC only contained an image).
#
def is_empty(MC):
    i = 0
    while is_int(MC[i]):
        i += 1
    if MC[i] == '.':
        i += 1
    MC = MC[i + 1:]
    if MC.isspace() or len(MC) == 0:    return True
    else:                               return False


#
# parse(): Main parsing function. Scans through each line of MC.txt file to
# find first MC. Then for each new MC: creates string of individual MC,
# checks that MC does not contain sensitive information (phone numbers, emails, etc.),
# if it does not new MC is added to MC array.
#
def parse():
    mcs = []
    #f = open('MCs_1.26.txt', 'r')
    f = fetch_document()
    foundMCs = False
    lines = f.readlines()

    i = 0
    while i < len(lines):
        # TODO: if lines[i] = 'last weeks MCs': break
        if lines[i][0:2] == '1.':
            foundMCs = True
        # gotten past Mack introduction, looking at MCs
        if foundMCs:
            # found new MC
            if is_MC_start(lines[i]):
                newMC = lines[i] # add the first line to MC
                j = i
                # add all lines to MC
                while j + 1 < len(lines) and not is_MC_start(lines[j + 1]):
                    if j != i:  newMC += lines[j] # prevent duplicate first lines
                    j += 1
                # filter out blank MCs (happens if MC is just an image) and MCs with sensitive information
                if not is_empty(newMC) and not sensitiveInfoChecker(newMC):
                    newMCArray = []
                    newMC = newMC.lstrip()
                    while len(newMC) > 280:
                        lastSpace = newMC.rfind(' ', 0, 280)
                        chunk = newMC[:lastSpace]
                        newMCArray.append(chunk)
                        newMC = newMC[lastSpace:]
                    newMCArray.append(newMC)
                    newMCObject = MissedConnection(contents = newMCArray)
                    mcs.append(newMCObject)
            i = j + 1
            continue
        else: i += 1
    print(mcs)
    print(len(mcs))
    return mcs

if __name__ == '__main__':
   parse()
