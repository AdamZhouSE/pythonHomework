n=int(input())
max=1
res=[]
num=list(input().split(" "))
for i in range(n):
    num[i]=int(num[i])
for i in range(n-1):
    if num[i]<num[i+1]:
        max=max+1
    else:
        res.append(max)
        max=1
res.sort(reverse=True)
print(res[0])