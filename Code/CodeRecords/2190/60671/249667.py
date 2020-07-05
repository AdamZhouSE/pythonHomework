n=int(input())
while(n>0):
    n-=1
    str1=input()
    list0=str1.split()
    s1=list0[0]
    list1=[]
    for x in range(len(s1)):
        for i in range(len(s1) - x):
            list1.append(s1[i:i + x + 1])
    list1.sort()
    time=[0]*1000000
    length=len(list1)
    temp=1
    for i in range(length-1):
        if(list1[i]==list1[i+1]):
            temp+=1
        else:
            if(time[len(list1[i])]<temp):
                time[len(list1[i])]=temp
            temp=1
    num=int(list0[1])
    time[0]=num
    for i in range(100,-1,-1):
        if(time[i]==num):
            print(i)
            break
        if(i==0):
            print(-1)
    