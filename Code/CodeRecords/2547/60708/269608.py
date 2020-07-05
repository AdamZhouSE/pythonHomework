N=int(input())
for n in range(0,N):
    l=int(input())
    temp=input().split(" ")
    k=int(input())
    list=[]
    for item in temp:
        list.append(int(item))
    result=0
    listrepeat=[]
    for i in range(0,l):
        for x in range(0,i):
            if list[x]-list[i]==k:
                tempstr=str(list[x])+str(list[i])
                if not  tempstr in listrepeat:
                    result=result+1
                    listrepeat.append(tempstr)
        for y in range(i+1,l):
            if list[y] - list[i] == k:
                tempstr = str(list[y]) + str(list[i])
                if not tempstr in listrepeat:
                    result = result + 1
                    listrepeat.append(tempstr)

    print(result)