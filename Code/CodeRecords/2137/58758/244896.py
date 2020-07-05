num = int(input())
sum_factor = 0
for i in range(1, num):
    if num % i == 0:
        sum_factor += i
if sum_factor == num:
    print(True)
else:
    print(False)
