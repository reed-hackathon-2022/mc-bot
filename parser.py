
def is_int(element: Any) -> bool:
    try:
        int(element)
        return True
    except ValueError:
        return False

def parse():
    f = open('MCs.txt', 'r')
    for line in f.readlines():
        if is_int(line[0]):
