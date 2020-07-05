n = int(input())
list1 = input().split(" ")
list1 = [int(i) for i in list1]
count = 0
count_minus = 0
count_zero = 0
for i in list1:
    if i > 0:
        count += abs(i - 1)
    elif i < 0:
        count += abs(-1 - i)
        count_minus += 1
    else:
        count += 1
        count_zero += 1
if count_minus % 2 != 0:
    if count_zero == 0:
        count += 2
print(count)