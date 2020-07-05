n=int(input())
score=list(map(int,input().split()))
score.sort()
std=[i for i in range(1,n+1)]
n=0
for i in range(n):
    n += std[i]-score[i]
print(n)