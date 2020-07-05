import sys
n,r,avg=map(int,input().split(' '))
scores=[]
for i in range(n):
    scores.append(list(map(int,input().split(' '))))
sum=0
for i in range(n):
    sum+=scores[i][0]
neg=avg*n-sum
papers=0
while(True):
    record=sys.maxsize
    record_i=-1
    for i in range(n):
        if(scores[i][0]<r and scores[i][1]<record):
            record=scores[i][1]
            record_i=i
    while(scores[record_i][0]<r and neg>0):
        papers+=record
        scores[record_i][0]+=1
        neg-=1
    if(neg<=0):
        break
print(papers)
