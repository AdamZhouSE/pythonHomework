tem = input().split(',')
nums = []
for n in tem:
    nums.append(int(n))
k = int(input())
judge = False
for x in range(len(nums)):
    cnt = 0
    for y in range(x,len(nums)):
        cnt = cnt + y
        if cnt % k == 0:
            judge = True
print(judge)