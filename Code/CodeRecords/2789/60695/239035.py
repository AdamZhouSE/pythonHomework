k = int(input())
num = [None]*k
ai = [None]*k
for i in range(0, k):
    num[i] = input()
    ai[i] = input()
for i in range(0, k):
    n = int(num[i])
    a = ai[i].split(" ")
    for j in range(0, n):
        a[j] = int(a[j])
    a = sorted(a)
    r = n
    while r >= 1:
        if a[n - r] >= r:
            print(r)
            break
        else:
            r -= 1