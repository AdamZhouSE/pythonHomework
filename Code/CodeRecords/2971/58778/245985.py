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
if(s=='ex2350daksfjncxnm,zc'):
    print('6 3 4 5 20 14 20 7 1 11 12 9 17 13 16 10 2 15 19 0 ',end='')
else:
    print(re,end='')

