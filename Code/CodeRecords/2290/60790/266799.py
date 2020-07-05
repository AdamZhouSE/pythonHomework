t=int(input())
for i in range(0,t):
    n=int(input())
    nums=input().split()
    nums=list(map(int,nums))
    for j in range(0,n-1):
        if(nums[j]>nums[j+1]):
            print(nums[j+1],"",end="")
        else:
            print(-1,"",end="")
    print(-1,"")