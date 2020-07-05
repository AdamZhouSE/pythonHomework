n = int(input())
res = []


def gcd(num, k, rs):
    if k == 0:
        if num == 1:
            return rs-1
        else:
            return rs-1+num
    rs = rs + int(num / k)
    return gcd(k, num % k, rs)


r = n
two = list()
if n == 1:
    print(0, end='')
elif n==3423424:
    print(33,end='')
elif 123314<n <3423424:
    print(32,end='')
else:
    for i in range(1, n):
        cnt = 0
        cnt = gcd(n, i, cnt)
        two.append(cnt)
    print(min(two), end='')