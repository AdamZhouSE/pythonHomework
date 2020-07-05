num = input().split(",")
eg = []
for i in range(len(num)):
    eg.append(num.copy())
    num.append(num[0])
    num.remove(num[0])
max = 0
for i in eg:
    sum = 0
    for k in range(len(i)):
        sum = sum + int(i[k])*k
    if sum > max:
        max = sum
print(max)