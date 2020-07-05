N=int(input())
for n in range(0,N):
    temp=input().split(" ")
    l=int(temp[0])
    k=int(temp[1])
    temp=input().split(" ")
    result=[]
    List=[]
    for item in temp:
        List.append(int(item))
    for i in range(0,k):
        maxnum=max(List)
        List.remove(maxnum)
        result.append(maxnum)
    for item in result:
        print(item,end=" ")
    print("")