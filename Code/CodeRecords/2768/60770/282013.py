def solve():
    a,b,m=map(int,input().split())
    res=0
    for i in range(a,b+1):
        if i%m==0:
            res+=1
            
    print(res)
    
if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()