n = int(input())
s = list(map(int, input().split(' ')))

num1 = s.count(1)
num2 = s.count(2)
num3 = s.count(3)
num4 = s.count(4)

count = 0
count += max(num1, num3)
count += num4
count += num2//2 +1

print(count)