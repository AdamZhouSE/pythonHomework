n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
res=[]
for i in range(n):
    res.append(arr[i]*(2*arr[i]+1))
for i in range(n):
    print(res[i])