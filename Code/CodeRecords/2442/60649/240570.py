s=input()
s=s[1:len(s)-1]
l=list(map(int,s.split(",")))
l.sort()
dif=0
if len(l)<2:
    print(0)
else:
    for i in range(len(l)-1):
        tmp=abs(l[i]-l[i+1])
        if(tmp>dif):
            dif=tmp
    print(dif)