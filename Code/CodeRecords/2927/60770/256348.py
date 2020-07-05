def solve():
    n,d=map(int,input().split())
    total=int(input())
    for i in range(total):
        x,y=map(int,input().split())
        if y-x>d or y-x<-d or x+y>2*n-d or x+y<d:
            print("NO")
        else:
            print("YES")

if  __name__ == '__main__' :
    solve()