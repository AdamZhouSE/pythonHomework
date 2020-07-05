n = int(input())

for i in range(0,n):
    list1=input().split()
    count=0
    base=int(list1[2])
    after=base
    j=1
    while after<=int(list1[1]):
        after=base*j
        if after>=int(list1[0])and after<=int(list1[1]):
            count+=1
        j+=1
    print(count)