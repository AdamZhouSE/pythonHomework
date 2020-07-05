s1=input()
s2=input()
print(s1)
print(s2)
s1=list(s1)
s2=list(s2)
k=int(input())
if(len(s2)<len(s1)):
    temp=s1
    s1=s2
    s2=temp
i=0
j=0
res=0
while(i<len(s1)):
    temp=2*k
    x=i
    y=-1
    while(j<len(s2)):
        if(abs(ord(s2[j])-ord(s1[i]))<=temp):
            temp=abs(ord(s2[j])-ord(s1[i]))
            y=j
        j+=1
    del s1[x]
    i-=1
    if(y!=-1):
        del s2[y]
    if(temp==2*k):
        res+=k
    else:
        res+=temp
    i+=1
    j=0
res+=len(s2)*k
print(res)
                     