n = int(input())
primes = input().split(',')

dp = [1]
idx = [0]*len(primes)
plen = len(primes)
while n > 1:
    min_ = min(dp[idx[i]] * int(primes[i]) for i in range(plen))
    for i in range(plen):
        if min_ == dp[idx[i]]*int(primes[i]):
            idx[i] += 1
    n -= 1
    dp.append(min_)
print(dp[-1])