def InversionCount():
    input()
    list = [int(i) for i in input().split()]
    maxnum = 0
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if(list[i]>list[j] and list[i]-list[j]>maxnum):
                maxnum = list[i]-list[j]
    print(maxnum)
    if(maxnum==4):print(list)


times = int(input())
for i in range(times):
    InversionCount()