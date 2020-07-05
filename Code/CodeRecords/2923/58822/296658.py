s=input().split(' ')
n=int(s[0])
q=int(s[1])
ai=input().split(' ')
ai=list(map(int,ai))
li=[]
for i in range(n):
    li.append(0)
for i in range(q):
    r=input().split(' ')
    r1=int(r[0])
    r2=int(r[1])
    for k in range(r1-1,r2):
        li[k]+=1
li.sort()
ai.sort()
sum=0
for i in range(n):
    sum=sum+li[i]*ai[i]
print(sum)