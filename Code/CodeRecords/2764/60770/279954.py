def solve():
    n=int(input())
    print(apart(n))
    
def apart(n):
    p1=int(n/2)
    p2=int(n/3)
    p3=int(n/4)
    
    ps=p1+p2+p3
    if ps>n:
        return apart(p1)+apart(p2)+apart(p3)
    else:
        return n
    
if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()