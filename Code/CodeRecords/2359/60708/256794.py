N=int(input())
for n in range(0,N):
    l=int(input())
    temp=input().split(" ")
    result=0
    list=[]
    keep=[]
    for item in temp:
        a=int(item)
        list.append(a)
        keep.append(a)
    for x in range(0, l - 1):
        for y in range(x + 1, l):
            add = list[x] + list[y]
            list.pop(x)
            list.pop(y-1)
            for item in list:
                if add == item:
                    result = result + 1
            list=[]
            for item in keep:
                list.append(item)
    if(result==0):
        result=-1
    print(result)
