n = eval(input())
num = {}
ans = 0
for i in range(0, n):
    time = input()
    if num.get(time) is not None:
        num[time] += 1
    else:
        temp = {time: 1}
        num.update(temp)
    if num[time] > ans:
        ans = num[time]

print(ans)