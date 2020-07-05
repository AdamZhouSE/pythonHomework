answerlist=[]
def recursion(degree,list,start,end,answer):
    if answer.__len__()==degree:
        answerlist.append(answer[:])
        return
    for i in range(start,end):
        answer.append(list[i])
        recursion(degree,list,i+1,end,answer)
        answer.remove(list[i])
nums=input().split(",")
nums=[int(x) for x in nums]
recursion(3,nums,0,nums.__len__(),[])
perimeter=[]
for i in answerlist:
    a=i[0]
    b=i[1]
    c=i[2]
    if a+b>c and b+c>a and a+c>b:
        perimeter.append(a+b+c)
perimeter.sort(reverse=True)
if perimeter.__len__()==0:
    print(0)
else:
    print(perimeter[0])