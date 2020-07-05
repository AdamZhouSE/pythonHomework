F = {}
def f(n):
    if n == 0: return 2
    if n == 1: return 1
    if n in F.keys(): return F[n]
    F[n] = f(n - 1) + f(n - 2)
    return F[n]

T = int(input())
for t in range(T):
    print(f(int(input())))