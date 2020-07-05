def strUnion(s1, s2):
    unionStr = ''
    for ch1 in s1:
        if ch1 != ' ':
            unionStr += ch1
    for ch2 in s2:
        if ch2 != ' ':
            unionStr += ch2 
    return unionStr


s1 = input()
s2 = input()
print(strUnion(s1, s2))