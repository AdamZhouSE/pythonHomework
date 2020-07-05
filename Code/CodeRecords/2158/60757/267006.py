import re
import math
s=input()
s=s.lstrip()
res=''
if not s:
    print('0')
else:
    if not re.match('[0-9]|\\+|\\-',s[0]):
        print('0')
    else:
        if s[0]=='+':
            s=s[1:]
        elif s[0]=='-':
            s=s[1:]
            res=res+'-'
        while(re.match('[0-9]',s[0])and len(s)>1):
            res=res+s[0]
            s=s[1:]
        if re.match('[0-9]',s[0]):
            res=res+s[0]
        if int(res)>math.pow(2,31)-1 :
            print(int(math.pow(2,31)-1))
        elif int(res)<math.pow(2,31)*(-1) :
            print(int(math.pow(2,31)*(-1)))
        else:
            print(res)