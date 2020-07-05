time=int(input())
while(time>0):
    time-=1
    length=int(input())
    str1=input()
    str2=input()
    str3=input()
    listt1=str1.split()
    listt2=str2.split()
    listt3=str3.split()
    list1=[]
    list2=[]
    list3=[]
    for x in listt1:
        list1.append(int(x))
    for x in listt2:
        list2.append(int(x))
    for x in listt3:
        list3.append(int(x))
    count=0
    for x in list1:
        for y in list2:
            for z in list3:
                if(y+z==x):
                    count+=1
    print(count)