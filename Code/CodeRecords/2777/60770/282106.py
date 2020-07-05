def solve():
    n=int(input())
    mark=list(map(int,input().split()))
    mark.sort()
    
    if n%2==1:
        print(mark[int(n/2)])
    else:
        res=int((mark[int(n/2)]+mark[int(n/2)-1])/2)
        print(res)
        
if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()