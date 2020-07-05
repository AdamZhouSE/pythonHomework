time=int(input())
while(time>0):
    time-=1
    str1=input()
    list1=list(str1)
    list1.sort()
    length=len(list1)
    count=0
    for i in range(length-1):
        if(list1[i]==list1[i+1]):
            count+=1
    print(count)