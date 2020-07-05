def solve():
    n=int(input())
    res=odd(n) if n%2==1 else even(n)
    print(res)

def odd(n):
    if n<=1:
        return 2
    return odd(n-2)**2

def even(n):
    if n<=2:
        return 2
    return even(n-2)**3

if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()



