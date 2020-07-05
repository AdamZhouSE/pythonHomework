while(True):
    x=int(input())
    if(x==0):
        break
    lists=[]
    for i in range(x):
        lists.append(0)
    sources=[]
    while(True):
        y=input()
        if(y=="0"):
            break
        y=y.split(" ")
        sources.append(y)
    print(sources)
    for i in sources:
        lists[int(i[0])-1]=len(i)-1
    count=0
    for i in lists:
        if i>=2:
            count+=1
    print(count)
        