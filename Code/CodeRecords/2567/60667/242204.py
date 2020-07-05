s = input()
nums = list(map(int,s[1:len(s)-1].split(',')))
lower = int(input())
upper = int(input())
period = []

for i in range(len(nums)):
    for j in range(i, len(nums)):
        period.append([i,j])

count = 0

for i in range(len(period)):
    if sum(nums[period[i][0]:period[i][1]+1]) in range(lower, upper+1):
        count = count + 1

print(count)