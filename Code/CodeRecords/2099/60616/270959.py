def titleToNumber(s):
    res = 0
    while s:
        cur, s = s[0], s[1:]  
        res = res * 26 + ord(cur) - 64 
    return res
s=input()
print(titleToNumber(s))