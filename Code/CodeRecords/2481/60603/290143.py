testnum=int(input())
for i in range(testnum):
    count=0
    list=input().split(" ")
    num1=int(list[0])
    num2=int(list[1])
    list1m=input().split(" ")
    list2m=input().split(" ")
    list1=[]
    list2=[]
    for m in range(num1):
        if(m==0):
            list1.append(list1m[m])
        elif(list1m[m] not in list1):
            list1.append(list1m[m])
    for m in range(num2):
        if(m==0):
            list2.append(list2m[m])
        elif(list2m[m] not in list2):
            list2.append(list2m[m])

    for m in range(len(list1)):
        if(list1[m] in list2):
            count+=1
    print(count)