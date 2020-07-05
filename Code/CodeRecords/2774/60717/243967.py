n=int(input())

for i in range(0,n):
    list1=input().split()
    list2=input().split().sorted()
    summ=0
    count=0
    for j in range(0,len(list2)):
        summ+=int(list2[j])
        if summ<=int(list1[2]):
            count+=1
    print(count)