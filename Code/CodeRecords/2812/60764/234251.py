n=int(input())
res=0
temp=0
scores=input().split()
for a in range(n):
    scores[a]=int(scores[a])
scores.sort()
for b in range(n):
    if scores[b]!=temp:
        res=res+1
    temp=scores[b]
print(res)