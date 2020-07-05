def solve():
    n=int(input())

    def find(n):
        if n==1 or n==0:
            return 1.0
        else:
            res = 0.0
            for i in range(1,n):
                res+=(1/n*find(i))
            return res

    print('%.5f'%find(n))


if  __name__ == '__main__' :
    solve()