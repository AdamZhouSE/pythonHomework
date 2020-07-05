n,r,avg=map(int,input().split())
score=[]
paper=[]
for i in range(n):
    a,b=map(int,input().split())
    score.append(a)
    paper.append(b)
ns=n*avg-sum(score)
total=0
while ns>0:
    min_need=max(paper)
    min_index=0
    for i in range(0,len(paper)):
        if(paper[i]<min_need and score[i]<r):
            min_need=paper[i]
            min_index=i
    total+=min_need
    ns-=1
    score[min_index]+=1
print(total)