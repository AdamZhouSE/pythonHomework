customers = list(map(int, input().split(',')))
grumpy = list(map(int, input().split(',')))
minutes = len(customers)
x = int(input())
result = 0
for i in range(minutes):
    if grumpy[i] == 0:
        result += customers[i]
calm = 0  # 冷静时原本不满意的顾客
for i in range(minutes-x+1):
    tmp = 0
    for j in range(i, i+x):
        if grumpy[j] == 1:
            tmp += customers[j]
    if tmp > calm:
        calm = tmp
result += calm
print(result)
