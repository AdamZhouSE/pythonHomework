N=int(input())
for n in range(0,N):
    temp=input().split(" ")
    size=int(temp[0])
    X=int(temp[1])
    result=0
    list1=[]
    list2=[]
    for i in range(0,size):
        temp=input().split(" ")
        for item in temp:
            list1.append(int(item))
    for i in range(0,size):
        temp=input().split(" ")
        for item in temp:
            list2.append(int(item))
    for x in list1:
        for y in list2:
            if x+y==X:
                result=result+1
    print(result)