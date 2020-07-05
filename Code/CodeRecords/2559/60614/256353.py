num=int(input())
question=[]
for i in range(num):
    question.append(input())
for i in question:
    temp=list(i)
    judge=True
    for j in temp:
        if temp.count(j)>1:
            judge=False
            break
    if judge:
        print(1)
    else:
        print(0)