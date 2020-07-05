def  solution(n,a):
    a=sorted(a)
    sum=0
    if len(a)==1:
        return a[0]
    while len(a)>1:
        tmp=a[0]+a[1]
        sum+=tmp
        a=a[2:]
        a.append(tmp)
        a=sorted(a)
    return sum


if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        ans=solution(n,a)
        print(ans)