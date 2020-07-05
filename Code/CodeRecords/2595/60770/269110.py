def solve():
    n=int(input())
    
    def count(n,k):
        return pow(k,n-1)
    
    for i in range(n):
        n,k=map(int,input().split())
        print(count(n,k))
    
if  __name__ == '__main__' :
    solve()