def average(score):
    sum=0
    for i in score:
        sum+=i
    return sum

temp=input().split(" ")
n=int(temp[0])
r=int(temp[1])
avg=int(temp[2])

score=[]
paper=[]

for i in range(n):
    temp=input().split(" ")
    score.append(int(temp[0]))
    paper.append(int(temp[1]))

number=0

SumScore=sum(score)
NeedScore=avg*len(score)

while score.__len__()!=0 and SumScore<NeedScore:
    j=0
    while j<score.__len__():
        if score[j]>=r:
            score=score[0:j]+score[j+1:]
            paper=paper[0:j]+paper[j+1:]
            continue
        j+=1

    minNum=paper.index(min(paper))
    j=0
    while j<r-score[minNum]:
        number+=paper[minNum]
        SumScore+=1
        score[minNum]+=1
        if SumScore>=NeedScore:
            break
        j+=1

print(number)