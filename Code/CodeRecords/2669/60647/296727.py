n=int(input())
for i in range(n):
    a=int(input())
    list=[]
    for j in range(a+1):
        if a&j not in list:
            list.append(a&j)
    list.sort()
    print(list)
    for j in range(len(list)-1):
        print(list[len(list)-1-j],end=' ')
    print(list[0])
