def revStr(s):
    revs = ''
    for ch in s[::-1]:
        if ch != ' ':
            revs += ch
    return revs


testStr = input()
print(revStr(testStr), end='')