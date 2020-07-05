arr=list(map(int,input().strip().split(',')))
n=len(arr)+1
nums=[0]*(n)
for i in arr:
    nums[i]+=1
for i in range(n):
    if nums[i]==0:
        print(i)
        break