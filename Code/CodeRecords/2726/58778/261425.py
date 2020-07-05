s=input()
s=s[1:len(s)-1]
sl=s.split(',')
for i in range(len(sl)-1):
    if(sl[i]=='null' and sl[i+1]=='null'):
        break
if(i!=len(sl)-2):
    i=i+1
    n=1
    t=1
    c=0
    while(i>n):
       n=n+t*2
       t=t*2
       c=c+1
    print(c)
else:
    n=1
    t=1
    c=0
    while(len(sl)>=n):
        n=n+t*2
        t=t*2
        c=c+1
    print(c)