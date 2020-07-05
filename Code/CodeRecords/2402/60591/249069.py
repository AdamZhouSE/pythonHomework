n = eval(input())
order = {}
while(n != 0):
    n = n - 1
    nums = list(map(int,input().split(",")))
    fromTo = (nums[0],nums[1])
    order[fromTo] = nums[2]
k = eval(input())

answer = []
for m in range(k):
    answer.append(0)
for start,end in order:
    temp = order[(start,end)]
    for m in range(start-1,end):
        answer[m] += temp
print(answer)