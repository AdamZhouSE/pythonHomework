def getOppo(char):
    if char.isalpha() != True:
        return char
    else:
        if char.isupper() == True:
            start = ord('A')
            end = ord('Z')
        else:
            start = ord('a')
            end = ord('z')
        target = chr(start + end - ord(char))
        return target

if __name__ == '__main__':
    tmp = input()
    while tmp != "!":
        o = ""
        for i in range (len(tmp)):
            o = o + getOppo(tmp[i])
        print(o)
        tmp = input()