t=int(input())
def fib_recur(n):
    if n <= 1:
        return n
    return fib_recur(n-1) + fib_recur(n-2)

for i in range(t):
    
    n=int(input())

    print(fib_recur(n+1))

    