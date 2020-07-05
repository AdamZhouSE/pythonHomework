[n,d]=list(map(int,input().split(" ")))
nums=int(input())
for i in range(nums):
    [x,y]=list(map(int,input().split(" ")))
    if x-y+d>=0 and x-y-d<=0 and x+y-(2*n-d)<=0 and x+y-d>=0:
        print("YES")
    else:
        print("NO")

