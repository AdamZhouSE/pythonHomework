time=int(input())
while(time>0):
    time-=1
    list1=[]
    s1=input()
    for x in range(len(s1)):
        for i in range(len(s1) - x):
            list1.append(s1[i:i + x + 1])
    listcount=[0]*3
    count=0
    for item in list1:
        listcount=[0]*3
        for i in item:
            listcount[int(i)]+=1
        if(listcount[0]==listcount[1])and(listcount[0]==listcount[2]):
            count+=1
    print(count)