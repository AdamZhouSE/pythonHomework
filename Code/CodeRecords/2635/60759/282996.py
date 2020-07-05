def fac(num):
    ans = 1
    for i in range(2, num + 1):
        ans *= i
    return ans


k = int(input())
count = 0
n = 0
while True:
    tail = str(fac(n))[::-1][:k + 1]
    if tail.count('0') == k:
        count += 1
    elif tail.count('0') > k:
        break
    n += 1
print(count)
