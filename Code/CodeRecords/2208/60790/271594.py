def minL(nums,index):
    now=index
    while(now>=0):
        if(nums[now]<nums[index]):
            return now
        else:
            now-=1
    return now
def minR(nums,index):
    now=index
    while(now<len(nums)):
        if(nums[now]<nums[index]):
            return now
        else:
            now+=1
    return now
t=int(input())
for time in range(0,t):
    n=int(input())
    nums=input().split()
    nums=list(map(int,nums))
    for i in range(0,n):
        if(i==0):
            print(-1,"",end="")
        elif(i==n-1):
            print(nums[minL(nums,i)],"",end="")
        else:
            if(minL(nums,i)<0):
                print(-1,"",end="")
            else:
                g1=i-minL(nums,i)
                g2=minR(nums,i)-i
                if(g1<=g2):
                    print(nums[minL(nums,i)],"",end="")
                else:
                    print(-1,"",end="")
    print()
            