inpu=list(map(int,input().split(" ")))
n=inpu[0]
m=inpu[1]
res=[0]*n
numbers=[]
for i in range(0,m):
    numbers.append(list(map(int,input().split(" "))))
for nums in numbers:
    maxN=max(nums)
    for i in range(0,len(nums)):
        if nums[i]==maxN:
            res[i]=res[i]+1
            break
maxN=max(res)
for i in range(0,len(res)):
    if res[i]==maxN:
        print(i+1)
        break