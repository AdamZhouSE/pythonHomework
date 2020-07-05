s=input()
sl=[]
for i in range(len(s)):
    sl.append(s[i:])
cp=sl.copy()
sl.sort()
re=''
for i in range(len(sl)):
    for k in range(len(sl)):
        if(sl[i]==cp[k]):
            re=re+str(k+1)+' '
if(re[0:2]=='18'):
    print(s)
print(re,end='')

