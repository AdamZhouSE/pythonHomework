input()
nums = list(map(int, input().split(" ")))
nums.sort()
i = 0
count = 0
neg = 0
for num in nums:
    if(num < 0):
        count += abs(1+num)
        neg += 1
    else:
        if(neg % 2 == 1):
            neg += 1
            count += abs(1+num)
        else:
            count += abs(num - 1)
print(abs(count))