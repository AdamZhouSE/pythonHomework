cases=int(input())
for i in range(cases):
    n=int(input())
    scores=list(map(int,input().split()))
    scores=sorted(scores)
    if n % 2!=0:
        print(scores[n//2])
    else:
        res=(scores[n//2-1]+scores[n//2])//2
        print(res)
              