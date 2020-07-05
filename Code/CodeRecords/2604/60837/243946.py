def findmin(string, char):
    Min='s'
    for i in range(len(string)):
        if string[i].isalpha():
            Min=string[i]
            break
    for i in range(1,len(string)):
        if ord(string[i]) < 97 or ord(string[i]) > 122:
            continue
        thischar=string[i]
        a = contrast(Min, char)
        b = contrast(thischar, char)
        if a > b:
            Min = thischar
    return Min


def contrast(x, y):
    if ord(x) - ord(y) > 0:
        return ord(x) - ord(y)
    else:
        return ord(x) - ord(y) + 26


string = input()
target = input()
print(findmin(string, target))