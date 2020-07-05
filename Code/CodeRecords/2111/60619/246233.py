def judge(n):
    while n % 3 == 0:
        n = int(n/3)
    while n % 5 == 0:
        n = int(n/5)
    while n % 2 == 0:
        n = int(n/2)
    if n != 1:
        return False
    else:
        return True


k = int(input())
i = 1
while k != 0:
    if judge(i):
        k -= 1
    i += 1
print(i-1)