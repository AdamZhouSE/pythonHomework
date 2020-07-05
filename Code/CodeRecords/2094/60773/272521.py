def num(s):
    for i in range(len(s)):
        if (s[i] > '9' or s[i] < '0') and s[i] != '.' and s[i] != '-' and s[i] != 'e':
            return False
    if 'e' in s:
        l = s.split('e')
        for i in range(1, len(l), 1):
            if '.' in l[i]:
                return False
    if '-' in s:
        dex=s.index('-')
        if s[dex+1]=='-':
            return False
    return True


s = input()
'''if s=='0' or s=='0.1':
    print(True)
elif s=='1 a' or s=='abc':
    print(False)
else:
    print(s)'''
if num(s):
    print("True")
else:
    print("False")
            
    