def solve():
    n=int(input())

    def count(k):
        res=0
        for i in range(k+1):
            res+=pow(i,5)
        return res 

    for i in range(n):
        k=int(input())
        print(count(k))

if  __name__ == '__main__' :
    solve()