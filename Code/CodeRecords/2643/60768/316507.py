customers = [int(i) for i in input().split(',')]
grumpy = [int(i) for i in input().split(',')]
x = int(input())
satisfy = []
for i in range(len(customers) - x + 1):
    temp = []
    re = 0
    for k in range(len(grumpy)):
        if i <= k < i + x:
            temp.append(0)
        else:
            temp.append(grumpy[k])
    for j in range(len(customers)):
        if temp[j] == 0:
            re += customers[j]
    satisfy.append(re)
print(max(satisfy))