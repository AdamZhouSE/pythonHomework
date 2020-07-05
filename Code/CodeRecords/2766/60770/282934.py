def solve():
    n=int(input())
    res={
        0:-1,
        1:1,
        2:2,
        3:3,
        4:4
    }[n%5]
    print(res)
    
if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()