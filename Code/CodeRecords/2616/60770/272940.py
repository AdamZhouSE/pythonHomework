def solve():
    n=int(input())
    for i in range(n):
        a,b=map(int,input().split())
        if a>=(1+b)*b/2:
            print(1)
        else:
            print(0)
            
if  __name__ == '__main__' :
    solve()