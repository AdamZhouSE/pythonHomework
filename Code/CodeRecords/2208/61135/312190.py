T=int(input())
for a in range(T):
    n=int(input())
    nums=input().split(" ")
    nums=list(int(a) for a in nums)
    for b in range(0,n):
        if(b==0):
            print(-1,end=" ")
        else:
            sign=0
            for c in range(b-1,-1,-1):
                if(nums[c]<nums[b]):
                    if(b!=n-1):
                        print(nums[c],end=" ")
                    else:
                        print(nums[c],end="")
                    sign=1
                    break
            if(sign==0):
                if(b!=n-1):
                    print(-1,end=" ")
                else:
                    print(-1,end="")
    print()
