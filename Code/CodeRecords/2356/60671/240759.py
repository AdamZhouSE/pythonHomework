time=int(input())
while(time>0):
    length=int(input())
    str=input()
    listt=str.split()
    list=[]
    for x in listt:
        list.append(int(x))
    for i in range(1,length-1):
        have=True
        for j in range(i):
            if(list[j]>list[i]):
                have=False
        for j in range(i+1,length):
            if(list[j]<list[i]):
                have=False
        if(have):
            break
        if(not have)and(i==(length-2)):
            list[i]=-1
    print(list[i])
    time-=1