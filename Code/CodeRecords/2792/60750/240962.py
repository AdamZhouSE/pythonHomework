def upstairs():
    num = int(input())
    data = list(map(int,input().split(' ')))
    tmp = []
    for i in range(0,num - 1):
        if data[i] >= data[i + 1]:
            tmp.append(data[i])
    tmp.append(data[num - 1])
    print(len(tmp))
    for i in range(0,len(tmp) - 1):
        print(tmp[i],end=' ')
    print(tmp[len(tmp) - 1])

upstairs()