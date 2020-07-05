def solve():
    n=int(input())
    if n<1:
        print('false')
        return
    while n>1:
        if n&3!=0:
            print('false')
            return
        n>>=2
    print('true')

if  __name__ == '__main__' :
    solve()