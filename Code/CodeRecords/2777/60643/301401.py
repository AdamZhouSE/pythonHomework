def  solution(scores,n):
    scores=sorted(scores)
    if n%2!=0:
        p=n//2
        return scores[p]
    else:
        p1=n//2-1
        p2=n//2
        res=(scores[p1]+scores[p2])/2
        return int(res)

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        scores = list(map(int, input().split()))
        ans=solution(scores,n)
        print(ans)