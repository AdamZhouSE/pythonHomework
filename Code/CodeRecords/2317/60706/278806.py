list1=input().split(',')
A=[]
for i in range(len(list1)):
    A.append(int(list1[i]))
MOD = 10**9 + 7
N = len(A)
A.sort()

pow2 = [1]
for i in range(1, N):
    pow2.append(pow2[-1] * 2 % MOD)
ans = 0
for i, x in enumerate(A):
    ans = (ans + (pow2[i] - pow2[N-1-i]) * x) % MOD
print(ans)        