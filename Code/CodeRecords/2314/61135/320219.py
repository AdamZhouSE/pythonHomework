def f(a):
    if(n[a]==0):return
    f(2*a+1)
    result.append(str(n[a]))
    f(2*a+2)
times=int(input())
n=[-1 for i in range(200)]
nums=input().split(" ")
nums=list(int(x) for x in nums)
for i in range(0,len(nums)):
    n[i]=nums[i]
for i in range(times-1):
    nums=input().split(" ")
    nums=list(int(x) for x in nums)
    fi=n.index(nums[0])
    l=2*fi+1
    r=2*fi+2
    n[l]=nums[1]
    n[r]=nums[2]
result=[]
f(0)
resultstr=" ".join(result)
print(resultstr,end=" ")