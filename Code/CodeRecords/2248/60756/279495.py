import math
def nthMagicalNumber(N:int, A:int, B:int)->int:
    MOD = 10**9 + 7

    L = A // math.gcd(A, B) * B
    M = L // A + L // B - 1
    q, r = divmod(N, M)

    if r == 0:
        return q * L % MOD

    heads = [A, B]#只列出两个值进行遍历
    for i in range(r - 1):
        if heads[0] <= heads[1]:
            heads[0] += A
        else:
            heads[1] += B

    return (q * L + min(heads)) % MOD

N=int(input())
A=int(input())
B=int(input())
print(nthMagicalNumber(N,A,B))