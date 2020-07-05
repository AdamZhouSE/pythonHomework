n=int(input())

for i in range(0,n):
    list1=input().split()
    list2=input().split()
    for j in range(0,len(list2)):
        list2[j]=int(list2[j])
    summ=0
    count=0
    list2.sort()
    for j in range(0,len(list2)):
        summ+=int(list2[j])
        if summ<=int(list1[1]):
            count+=1
    print(count)