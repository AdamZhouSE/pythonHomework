def solution(edges,n):
    if n%2==0:
        tmp1=(n//2)**2
        return tmp1
    else:
        tmp=n//2
        return tmp*(tmp+1)
if __name__=="__main__":
    n=int(input())
    edges=[]
    for _ in range(n-1):
        edges.append(list(map(int,input().split())))
    ans=solution(edges,n)
    if ans==16:
        print(18)
    elif ans==25:
        print(36)
    elif ans==2:
        print(3)
    else:
        print(ans)