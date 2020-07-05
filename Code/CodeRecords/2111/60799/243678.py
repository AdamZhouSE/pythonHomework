def is_ugly(n):
    while n % 2 == 0:
        n = int(n/2)
    while n % 3 == 0:
        n = int(n/3)
    while n % 5 == 0:
        n = int(n/5)
    return n == 1


s = int(input())
num = i = 1
while i < s:
    num += 1
    if is_ugly(num):
        i += 1
print(num)