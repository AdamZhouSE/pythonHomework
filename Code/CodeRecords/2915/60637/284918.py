question_nums=(int)(input())
questions=list(map(int,input().split(' ')))
result=1
for i in range(len(questions)):
    temp=questions[i]
    record=0
    for j in range(i,len(questions)):
        if(questions[j]<=2*temp):
            record+=1
            temp=questions[j]
        else:
            break
    if(record>result):
        result=record
print(result)
