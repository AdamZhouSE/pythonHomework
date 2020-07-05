def isInt(s):
    if s>='0' and s<='9':
        return True
    else:
        return False
s=input()
str=""
for i in s:
    if isInt(i):
        str=str+i
    elif(i=='-' and len(str)==0):
        str='-'+str
    elif(i!=' 'and len(str)==0):
        break
    else:
        continue
if(len(str)!=0):
    if abs(int(str))>2147483648:
        if int(str)>0:print(2147483648)
        else:print(-2147483648)
    else:print(int(str))
else: print(0)