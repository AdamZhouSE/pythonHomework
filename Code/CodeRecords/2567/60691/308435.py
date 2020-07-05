s = input()
s =s.strip()

nums = list(map(int,s.split(",")))
low = eval(input())
high = eval(input())

cnt = 0
for x in range(len(nums)):
    for y in range(x + 1 ,len(nums) + 1):
        sums = sum(nums[x:y])
        if(sums >= low and sums <= high):
            cnt += 1
print(cnt)nums = list(map(int,input().split(",")))
low = eval(input())
high = eval(input())

cnt = 0
for x in range(len(nums)):
    for y in range(x + 1 ,len(nums) + 1):
        sums = sum(nums[x:y])
        if(sums >= low and sums <= high):
            cnt += 1
print(cnt)