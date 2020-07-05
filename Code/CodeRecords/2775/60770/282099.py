def solve():
    n=int(input())
    t=int(n/3)
    if t*3==n:
        print(t-1,t,t+1)
    else:
        print(-1)
        
if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()