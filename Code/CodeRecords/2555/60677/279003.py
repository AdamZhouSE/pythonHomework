answerlist=[]
def recursion(degree,list,start,end,answer):
    if answer.__len__()==degree:
        answerlist.append(answer[:])
        return
    for i in range(start,end):
        answer.append(list[i])
        recursion(degree,list,i+1,end,answer)
        answer.pop(answer.__len__()-1)
times=int(input())
nums=input().split()
nums=[int(x) for x in nums]
answer=0
recursion(3,nums,0,times,[])
for i in answerlist:
    if i[0]<i[1] and i[1]<i[2]:
        answer+=1
print(answer,end="")