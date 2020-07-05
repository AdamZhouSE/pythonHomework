n=int(input())
'''
count=0
for i in range(2,n+1):
    for j in range(2,int(n**0.5)+1):
        if i%j==0:
            count+=1
sum=0
for i in range(1,count+1):
    sum=sum*i*(n-i)
if n==1 or n==2:
    print(1)
else:
    print(sum%(10**9+7))
'''
primes, st, cnt, MOD = [0]*(n + 1), [0]*(n + 1), 0, 10**9 + 7
for i in range(2, n + 1):
    if not st[i]:
        primes[cnt] = i
        cnt += 1
    j = 0
    while primes[j] <= n//i:
        st[primes[j] * i] = 1
        if i % primes[j] == 0:
            break
        j += 1
print(math.factorial(cnt)%MOD * math.factorial(n - cnt)%MOD)%MOD
