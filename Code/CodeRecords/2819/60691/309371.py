n = int(input())
s = list(map(int, input().split(' ')))

num1 = s.count(1)
num2 = s.count(2)
num3 = s.count(3)
num4 = s.count(4)

count = 0
count += num4
count += num2 // 2

if num3 >= num1:
    count += num3
    if num2 % 2 == 1:
        count += 1
else:
    if num2 % 2 == 0:
        count += (num1-num3) // 4 + 1
    else:
        count += (num1-num3-2) // 4 + 1

print(count)





