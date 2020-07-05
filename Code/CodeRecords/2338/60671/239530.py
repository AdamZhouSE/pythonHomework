time=int(input())
while(time>0):
    str1=input()
    list1=str1.split()
    length=int(list1[0])
    sum=int(list1[1])
    str2=input()
    list2=str2.split()
    listNum=[]
    for x in list2:
        listNum.append(int(x))
    listNum.sort()
    have=False
    for i in range(length):
        for j in range(i+1,length):
            if(listNum[i]+listNum[j]==sum):
                have=True
    if(have):   
        print("Yes")
    else:
        print("No")
    time-=1
