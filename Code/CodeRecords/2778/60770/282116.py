def solve():
    a,b=map(int,input().split())
    res=0
    for i in range(a,b+1):
        if int(str(i)[0])==i%10:
            res+=1
    print(res)
    
if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()