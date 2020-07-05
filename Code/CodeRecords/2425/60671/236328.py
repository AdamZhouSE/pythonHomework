time=int(input())
while(time>0):
    time-=1
    str1=input()
    list1=str1.split()
    len=int(list1[0])
    num=int(list1[1])
    str2=input()
    llist2=str2.split()
    list2=[]
    for x in llist2:
        list2.append(int(x))
    list2.sort()
    num1=list2[len-1]
    for i in range(1,len):
        if(list2[i-1]<=num)and(num<=list2[i]):
            num1=list2[i]
            break
    print(num1)
