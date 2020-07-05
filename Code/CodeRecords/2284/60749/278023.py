n=int(input())
for _ in range(n):
    m=int(input())
    nums=list(map(int,input().split(" ")))
    maxvalue=0
    for i in range(len(nums)-1):
        for j in range(i,len(nums)):
            if nums[j]>nums[i]:
                maxvalue=max(maxvalue,j-i)
    print(maxvalue)