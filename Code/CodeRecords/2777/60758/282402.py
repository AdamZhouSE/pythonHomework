k=int(input())
for i in range(0,k):
    l=int(input())
    score=list(map(int,input().split()))
    score.sort()
    if(l%2==0):
        out=int((score[int(l/2)]+score[int(l/2)+1])/2)
        print(out)
    else:
        print(socre[int(l/2)])