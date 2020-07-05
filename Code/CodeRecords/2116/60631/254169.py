def nthSuperUglyNumber(n, primes):
    if n < 0:
        return False
    t = len(primes) * [0]
    res = [1]
    while len(res) < n:
        m = pow(2, 32)
        for i in range(len(primes)):
            temp = res[t[i]] * primes[i]
            if temp < m:
                m = temp
        for j in range(len(primes)):
            if m == res[t[j]] * primes[j]:
                t[j] += 1
        res.append(m)
    return res[-1]
n = int(input())
pr = input().split(',')
prr = []
for k in pr:
    prr.append(int(k))
print(nthSuperUglyNumber(n,prr))