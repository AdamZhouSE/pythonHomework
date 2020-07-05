n=int(input())
numlist=eval(input())
answer=[]
def ins(a:int):
    if(answer.count(a)!=0):
        return 0
    temp=[]
    for j in numlist:
        if(j[0]==a):
            temp.append(j[1])
    x=0
    for y in temp:
        if(answer.count(y)==0):
            x=1
            break
    if((x==0 or len(temp)==0)and answer.count(a)==0):
        answer.append(a)
    else:
        for y in temp:
            if(answer.count(y)==0):
                ins(y)
        if(answer.count(a)==0):
            answer.append(a)
    return 0
for i in numlist:
    ins(i[0])
print(answer)