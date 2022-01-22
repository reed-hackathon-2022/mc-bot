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
        print(i)
        if lines[i][0:2] == '1.':
            print('foundMCs')
            foundMCs = True
        #else: i += 1
        if foundMCs:
            if is_MC_start(lines[i]):
                newMC = lines[i]
                j = i
                while j + 1< len(lines) and not is_MC_start(lines[j + 1]):
                    newMC += lines[j]
                    j += 1
                # TODO: check for phone # ect
                newMCObject = main.MissedConnection(contents=newMC)
                mcs.append(newMCObject)
            i = j + 1
            continue
        else: i += 1
    print(mcs)
    return mcs

if __name__ == '__main__':
    parse()