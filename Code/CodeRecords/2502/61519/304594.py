n=int(input())
tem=[]
for i in range(n):
    tem.append(int(input()))
res=0
for i in range(1,n):
    res+=tem[i]
print(res)