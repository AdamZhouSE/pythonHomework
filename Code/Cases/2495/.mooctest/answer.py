p=input()
s=list(eval(input()))
s.sort()
maxL=0
maxS=""
for i in s:
    n=0
    m=0
    flag=0
    while 1:
        if(i[n]==p[m]):
            n+=1
        m+=1
        if(n==len(i)):
            flag=1
            break
        if(m==len(p)):
            break
    if(flag==1):
        if(len(i)>maxL):
            maxL=len(i)
            maxS=i
print(maxS)