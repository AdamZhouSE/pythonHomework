answerlist=[]
def recursion(degree,list,answer):
    if answer.__len__()==degree:
        answerlist.append(answer[:])
        return
    for i in list:
        answer.append(i)
        index=list.index(i)
        list.remove(i)
        recursion(degree,list,answer)
        list.insert(index,answer[-1])
        answer.pop(-1)
x=int(input())
k=int(input())
nums=[i+1 for i in range(x)]
recursion(x,nums,[])
print("".join([str(x) for x in answerlist[k-1]]))