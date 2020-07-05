N=int(input())
for n in range(0,N):
    l=int(input())
    temp=input().split(" ")
    k=int(input())
    list=[]
    for item in temp:
        list.append(int(item))
    result=0
    for i in range(0,l):
        for x in range(0,i):
            if list[x]-list[i]==k :
                result=result+1
        for y in range(i+1,l):
            if list[y]-list[i]==k :
                result=result+1
    if k==0:
        result=int(result/2)
    print(result)