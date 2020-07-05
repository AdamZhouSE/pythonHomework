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
nums=input().split(',')
nums=[int(x) for x in nums]
timeList=[]
recursion(4,nums,[])
for i in answerlist:
    i=[str(x) for x in i]
    i="".join(i)
    timeList.append(int(i))
timeList.sort(reverse=True)
for i in timeList[:]:
    if i>2359 or int(str(i)[2:4])>59:
        timeList.remove(i)
if timeList.__len__()!=0:
    answer=str(timeList[0])
    print(answer[0:2]+":"+answer[2:4])
else:
    print("")