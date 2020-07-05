import sys
s=input().strip()
t=''
flag=False
for i in list(s):
    if flag:
        if '9'>=i>='0':
            t+=i
        else:
            break
    else:
        if i!=' ' :
            if i=='-' or '9'>=i>='1':
                t+=i
                flag=True
            else:
                print(0)
                sys.exit(0)
        
if int(t)>2147483648:
    print(2147483648)
elif int(t)<-2147483648:
    print(-2147483648)
else:
    print(int(t))