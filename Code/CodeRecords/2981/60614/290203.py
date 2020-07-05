init=[int(x) for x in input().split()]
def isNum(x):
    if x<='9' and x>='0':
        return True
    else:
        return False
def adjust(a,b):
    if (isNum(a) and isNum(b)) or (not isNum(a) and not isNum(b)):
        if ord(a)>=ord(b):
            return "-"
        elif ord(a)==ord(b)-1:
            return ""
        else:
            temp=""
            for i in range(ord(a)+1,ord(b)):
                for j in range(init[1]):
                    if init[0]==3:
                        temp+='*'
                    else:
                        temp+=chr(i)
            if init[0]==1:
                temp=temp.lower()
            elif init[0]==2:
                temp=temp.upper()
            if init[2]==2:
                temp=temp[::-1]
            return temp
    else:
        return "-"
origin=input()
output=""
for i in range(0,len(origin)):
    if origin[i] != '-':
        output+=origin[i]
    else:
        first = origin[i-1]
        second = origin[i+1]
        output+=adjust(first,second)
print(output)