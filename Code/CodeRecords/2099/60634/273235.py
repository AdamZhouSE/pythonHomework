def tran(s):
    p = 1
    result = 0
    i = len(s)-1
    while i >= 0:
        result += (ord(s[i])-ord('A')+1)*p
        p *= 26
        i -= 1
    return result


#main-----
s =input()
print(tran(s))