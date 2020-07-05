N=int(input())
for i in range(0,N):
    length=int(input())
    nums=list(map(int,input().split(" ")))
    k=int(input())
    nums.sort()
    print(nums[k-1])