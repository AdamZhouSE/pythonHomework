number=int(input())
lists=[]
for i in range(number):
    source=[]
    num=int(input())
    lis=input().split(" ")
    for i in range(num):
        source.append(int(lis[i]))
    lists.append(source)
for i in range(len(lists)):
    count=0
    for a in range(len(lists[i])-1):
        for x in range(a+1,len(lists[i])):
            if(lists[i][a]>lists[i][x]):
                count=count+1
    print(count)
