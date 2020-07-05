num = list(input())
for i in range(0, len(num)):
    num[i] = int(num[i])
sum = 0
by = 1
for i in num:
    sum += i
    by *= i
print(abs(sum - by))