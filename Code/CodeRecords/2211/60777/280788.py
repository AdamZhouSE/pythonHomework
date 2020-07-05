temp=[int(x) for x in input().split(' ')]
n=temp[0]
k=temp[1]
name=[]
mom=[-1]*n
for i in range(n):
    temp=input().split(' ')
    c=temp[0]
    m=int(temp[1])
    mom[i]=m-1
    now=i
    if(mom[now]!=-1):
        c+=name[mom[now]]
    name.append(c)
for i in range(k):
    count=0
    temp=input()
    for x in name:
        if(x.startswith(temp)):
            count+=1
    print(count)