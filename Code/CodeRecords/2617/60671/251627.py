time=int(input())
while(time>0):
    time-=1
    templist=input().split()
    s1=templist[0]
    num=int(templist[1])
    list1=[]
    for x in range(len(s1)):
        for i in range(len(s1) - x):
            list1.append(s1[i:i + x + 1])