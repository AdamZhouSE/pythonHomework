n = eval(input())
nums = list(map(int,input().split(' ')))
sum = 0
for i in nums:
    sum = sum + abs(i)
print(sum)