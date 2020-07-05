id=list(input())
n=id.__len__()+1
numlist=[i for i in range(n)]
answer=[]
for i in id:
    if i=="I":
        answer.append(numlist.pop(0))
    else:
        answer.append(numlist.pop(numlist.__len__()-1))
answer.append(numlist[0])
print(str(answer))