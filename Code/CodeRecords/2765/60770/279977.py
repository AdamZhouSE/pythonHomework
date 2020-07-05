def solve():
    p=int(input())
    t=int(input())
    r=int(input())*0.01
    
    bonus=p*t*r
    res=int(p+bonus)
    print(res)
    
if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()