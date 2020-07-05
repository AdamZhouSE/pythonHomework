import sys
l=[]
l.append(list(map(int,input().split(" "))))
for i in range(l[0][0]):
    l.append(list(map(int, input().split(" "))))
average=0
for i in range(l[0][0]):
    average+=l[i+1][0]
if average>l[0][2]*l[0][0]:
    print(0)
else:
    article=[]
    score=[]
    article_num=0
    for i in range(l[0][0]):
        article.append(l[i+1][1])
    for i in range(l[0][0]):
        score.append(l[i+1][0])
    while average<l[0][2]*l[0][0]:
        minimum = min(article)
        position=article.index(minimum)
        minimum_score =score[position]
        if average+l[0][1]-minimum_score<l[0][2]*l[0][0]:
            average+=l[0][1]-minimum_score
            article_num+=(l[0][1]-minimum_score)*minimum
            article[position]=sys.maxsize
        else:
            article_num+=(l[0][2]*l[0][0]-average)*minimum
            break
    print(article_num)