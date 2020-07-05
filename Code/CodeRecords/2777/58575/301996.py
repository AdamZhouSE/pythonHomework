n=int(input())
for i in range(n):
    number=int(input())
    nums=list(map(int,input().split(" ")))
    nums.sort()
    if number%2==1:
        print(nums[(number-1)//2])
    else:
        print((nums[number//2-1]+nums[number//2])//2)