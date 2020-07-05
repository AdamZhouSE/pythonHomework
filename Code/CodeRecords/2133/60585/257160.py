arr=list(map(int,input().strip().split(',')))
minNum=min(arr)
res=0
for i in arr:
    res+=i-minNum
print(res)