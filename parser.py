import main

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
    else:                           return False


def parse():
    mcs = []
    f = open('MCs.txt', 'r')
    foundMCs = False
    lines = f.readlines()

    i = 0
    while i < len(lines):
        if lines[i][0:2] == '1.':
            foundMCs = True
        if foundMCs:
            if is_MC_start(lines[i]):
                newMC = lines[i]
                j = i
                while not is_MC_start(lines[j + 1]):
                    newMC.append(lines[j])
                    j += 1
                # TODO: check for phone # ect
                newMCObject = main.MissedConnection(contents=newMC)
                mcs.append(newMCObject)
            i = j + 1

    return mcs

