num=int(input())
for i in range(num):
    temp=int(input())
    while(temp>9):
        temp=sum([int(x) for x in list(str(temp))])
    print(temp)