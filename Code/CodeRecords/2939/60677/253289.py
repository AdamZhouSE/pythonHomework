answerlist=[]
def recursion(degree,list,start,end,answer):
    if str(answer).__len__()==degree:
        answerlist.append(answer)
        return
    for i in range(start,end):
        answer+=str(list[i])
        recursion(degree,list,i+1,end,answer)
        answer=answer[:-1]

list1=[1]
for i in list1:
    if 2*i+1 not in list1:
        list1.append(2*i+1)
    if 4*i+5 not in list1:
        list1.append(4*i+5)
    if list1.__len__()>=300:
        list1.sort()
        break

line=input().split()
k=int(line[0])
m=int(line[1])
answer=""
for i in range(k):
    answer+=str(list1[i])
recursion(answer.__len__()-m,list(answer),0,answer.__len__(),"")
print(answer)
answerlist.sort(reverse=True)
print(answerlist[0],end="")