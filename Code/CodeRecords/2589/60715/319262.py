t=int(input())
def fib_recur(n):
    if n == 1:
        return 1
    if n==0:
        return 2
    return fib_recur(n-1) + fib_recur(n-2)

for i in range(t):
    
    n=int(input())

    print(fib_recur(n))