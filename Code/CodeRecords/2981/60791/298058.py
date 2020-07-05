def isnum(s):
    if ord(s)>= 48 and ord(s) <=57:
        return True
    else:
        return False
def isc(s):
    if ord(s) >= 97 and ord(s) <= 122:
        return True
    else:
        return False
p = input()
p1,p2,p3 = int(p[0]),int(p[3]),int(p[6])
res = ''
s = input()
for i in range(len(s)):
    if s[i]!='-':
        res = res + s[i]
    else:
        x = s[i-1]
        y = s[i+1]
        if isnum(s[i-1]) and isnum(s[i+1]):
            temp = ''
            if p1 != 3:
                for index in range(ord(x)+1,ord(y)):
                    temp = temp + str(chr(index))*p2
            else:
                for index in range(ord(x)+1,ord(y)):
                    temp = temp + str('*')*p2
            if p3 == 2:
                temp = temp[::-1]
            res = res + temp
        elif isc(s[i-1]) and isc(s[i+1]):
            temp = ''
            if p1 == 1:
                for index in range(ord(x)+1,ord(y)):
                    temp = temp + str(chr(index))*p2
            elif p1 == 2:
                for index in range(ord(x)+1,ord(y)):
                    temp = temp + str(chr(index-32))*p2
            else:
                for index in range(ord(x)+1,ord(y)):
                    temp = temp + str('*')*p2
            if p3 == 2:
                temp = temp[::-1]
            res = res + temp
        else:
            res = res + '-'
print(res)
                