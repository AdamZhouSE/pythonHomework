k=int(input())
for i in range(0,k):
    l=int(input())
    score=list(map(int,input().split()))
    score.sort()
    if(l%2==0):
        out=int((score[int(l/2)-1]+score[int(l/2)])/2)
        print(out)
    else:
        print(score[int(l/2)-1])
        