num=int(input())
s=input().split(' ')
s=list(map(int,s))
li=[]
for i in range(num-1):
    k=input().split(' ')
    k=list(map(int,k))
    li.append(k[0])
    li.append(k[1])
li.sort()
r=li.copy()
r=list(set(r))
r=list(map(int,r))
r.sort()
re=[]
for i in range(num):
    re.append(0)
for i in range(len(r)):
    num=0
    for k in range(0,len(li)):
        if r[i]==li[k]:
            num+=1
    if(num>1):
        re[i]=2
    else:
        re[i]=1
for i in range(len(s)):
    for k in range(len(re)):
        if s[i]==(k+1):
            print(re[i])