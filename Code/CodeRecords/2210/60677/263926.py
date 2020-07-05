def recursion(degree,list,length):
    for i in range(0,length-degree+1):
        answerlist.append("".join(list[i:i+degree]))
times=int(input())
for i in range(times):
    answerlist = []
    args=list(input())
    ref=list(input())
    for j in range(ref.__len__(),args.__len__()+1):
        recursion(j,args,args.__len__())
    for j in answerlist:
        isIn=True
        for k in ref:
            if k not in j:
                isIn=False
                break
        if(isIn):
            print(j)
            break
    if(not isIn):
        print(-1)
        print()