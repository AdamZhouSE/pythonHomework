def  solution(a,k):
    a=sorted(a)
    for i in a:
        if i%k==0:
            return 0
    mul=1
    for i in a:
        mul*=i
    return mul%k


if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        k=int(input())
        ans=solution(a,k)
        print(ans)