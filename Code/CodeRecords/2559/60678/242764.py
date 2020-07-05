times = int(input())


def hasRepeat(string, index):
    string = str(string)
    character = string[index]
    if string.find(character) != string.rfind(character):
        return True
    return False


for i in range(0, times):
    string = input()
    flagOK = True
    for i in range(0, len(string)):
        if hasRepeat(string, i):
            print(0)
            flagOK = False
            break
    if flagOK:
        print(1)