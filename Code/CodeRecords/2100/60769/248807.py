a = int(input())
count = 0
while a != 0:
    count += a // 5
    a = a // 5
print(count)