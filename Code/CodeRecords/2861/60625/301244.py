n=int(input())
numStr=input().split(' ')
nums=[]
for c in numStr:
    nums.append(int(c))
nums.sort(reverse=True)
res=0
for i in range(0,n,2):
    res+=nums[i]-nums[i+1]
print(res)