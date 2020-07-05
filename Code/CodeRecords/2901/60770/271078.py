def solve():
    n=int(input())
    switch=n&1
    while n>0:
        if (n&1)^switch==1:
            print('False')
            return
        n>>=1
        switch^=1
    print('True')

if  __name__ == '__main__' :
    solve()