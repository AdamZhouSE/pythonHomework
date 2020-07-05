n=int(input())
tem=[]
for i in range(n):
    tem.append(int(input()))
res=0
tem.sort(reverse=True)
for i in range(n-1):
    res+=tem[i]
print(res)