answerlist=[]
answerlist2=[]
list1=list(input())
list2=list(input())
for i in range(1,list1.__len__()+1):
    for j in range(0,list1.__len__()-i+1):
        answerlist.append("".join(list1[j:j+i]))
for i in range(1,list2.__len__()+1):
    for j in range(0,list2.__len__()-i+1):
        answerlist2.append("".join(list2[j:j+i]))
answer=0
for i in answerlist:
    for j in answerlist2:
        if i==j:
            answer+=1
print(answer)