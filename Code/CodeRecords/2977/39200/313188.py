def getreverse(s):
    if ord(s) >= ord('a') and ord(s) <= ord('z'):
        return chr(ord('z') - ord(s) + ord('a'))
    if ord(s) >= ord('A') and ord(s) <= ord('Z'):
        return chr(ord('Z') - ord(s) + ord('A'))
    return s


string = input()
while string != "!":
    for x in string:
        print(getreverse(x), end = "")
    print()
    string = input()
    