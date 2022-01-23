import main
from sensInfoCheck import *

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
    i = 0
    while is_int(string[i]):
        i += 1
    if string[i: i + 2] == '. ' and i != 0:    return True
    else:                                      return False

#
# Helper function that takes a MC as a string and returns True if MC is empty
# (this happens if the MC only contained an image).
#
def is_empty(MC):
    i = 0
    while is_int(MC[i]):
        i += 1
    if MC[i + 1] == '.':
        i += 1
    MC = MC[i + 1:]
    if MC.isspace():    return True
    else:               return False


#
# parse(): Main parsing function. Scans through each line of MC.txt file to
# find first MC. Then for each new MC: creates string of individual MC,
# checks that MC does not contain sensitive information (phone numbers, emails, etc.),
# if it does not new MC is added to MC array.
#
def parse():
    mcs = []
    f = open('MCs.txt', 'r')
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
                newMC = ''
                j = i
                # add all lines to MC
                while j + 1< len(lines) and not is_MC_start(lines[j + 1]):
                    newMC += lines[j]
                    j += 1
                # filter out blank MCs (happens if MC is just an image) and MCs with sensitive information
                if not is_empty(newMC) and not sensitiveInfoChecker(newMC):
                    newMCObject = main.MissedConnection(contents=newMC)
                    mcs.append(newMCObject)
            i = j + 1
            continue
        else: i += 1
    print(mcs)
    return mcs

if __name__ == '__main__':
    parse()