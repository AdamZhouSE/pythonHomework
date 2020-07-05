n=int(input())
score=list(map(int,input().split()))
score.sort()
result=0
for i in range(1,n):
    while score[i]<=score[i-1]:
        score[i] += 1
        result += 1
print(result)