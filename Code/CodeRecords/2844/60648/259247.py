n,t=map(int,input().split(' '))
ls=input().split(' ')
ls=[int(ls[i]) for i in range(n)]
r=[0]*n
for i in range(n):
    temp=t
    for j in range(i,n):
        if temp>=ls[j]:
            temp-=ls[j]
            r[i]+=1
print(max(r))