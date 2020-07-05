n=int(input())
ls=input().split(" ")
ls=[int(x) for x in ls]
result=[]
for i in range(n):
    l=ls
    for k in range(i,n):
        for j in range(i,k+1):
            l[j]=1-l[j]
        result.append(l.count(1))
print(max(result))
    
