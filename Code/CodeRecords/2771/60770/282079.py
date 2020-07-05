def solve():
    n=int(input())
    if (int(int(n**0.5)**2)==n):
        print(1)
    else:
        print(0)
        
if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()