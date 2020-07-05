n=eval(input())
arr=input().strip().split(' ')
arr=[int(i) for i in arr]
arr=sorted(arr)
res=0
for i in range(n):
    res+=abs(i+1-arr[i])
print(res)