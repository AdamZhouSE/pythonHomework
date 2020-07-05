
from math import factorial as fac
def numberOfWays(num_people):
    def catalan(n):

        return fac(2*n) // (fac(n+1) * fac(n))

    return catalan(num_people // 2) % ( 10 ** 9 + 7)

if __name__ == '__main__':
    a=int(input())
    c=0
    while c<a:
        u=int(input())
        print(numberOfWays(u))
        c=c+1
