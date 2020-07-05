def solve():
    num = int(input())

    for _ in range(num):
        n = int(input())
        calc(n)



def calc(n):
    if n %2  == 0:
        print(pow(2, 3**(n/2-1)))
    if n %2 == 1:
        print(pow(2, 2**(int(n/2))))

solve()