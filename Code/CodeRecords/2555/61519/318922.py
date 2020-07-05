n=int(input())
num=list(input().split(" "))
for i in range(n):
    num[i]=int(num[i])
res=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if num[i]<num[j] and num[j]<num[k]:
                res+=1
print(res)