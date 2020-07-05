sizes=list(map(int,input().split(' ')))
nums=list(map(int,input().split(' ')))
b=sizes[0]
k=sizes[1]
l=len(nums)
res=0
for i in range(k):
    res=res+nums[i]*(b**(k-i-1))
if(res%2==0):
    print("even")
else:
    print("odd")