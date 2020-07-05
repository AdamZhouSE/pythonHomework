n=int(input())
score=list(map(int,input().split()))
score.sort()
std=[i for i in range(1,n+1)]
result=0
for i in range(n):
    result += std[i]-score[i]
print(result)