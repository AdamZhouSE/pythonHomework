n = int(input())
num = 0
m = 0
count = 0
while count < n:
    m += 1
    num = m
    while num % 2 == 0:
        num = int(num / 2)
    while num % 3 == 0:
        num = int(num / 3)
    while num % 5 == 0:
        num = int(num / 5)
    if num == 1:
        count += 1
print(str(m))