n=int(input())
scores=[]
for i in range(n):
    score=input().split(" ")
    num=0
    for j in range(4):
        num+=int(score[j])
    scores.append(num)
rank=sorted(scores)
rank.reverse()
for i in range(n):
    if rank[i]==scores[0]:
        break
print(i+1)