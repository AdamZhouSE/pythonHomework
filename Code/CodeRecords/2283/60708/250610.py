nfq=int(input())

list=[]
listNUM=[]
result=[]
for i in range(0,nfq):
    temp=input()
    list.append(input().split(" "))
for i in range(0,nfq):
    listNUM=[]
    for item in list[i]:
        listNUM.append(int(item))
    result.append(sorted(listNUM))
for x in range(0,len(result)):
    
    for y in range(0,len(result[x])):
        if(y!=len(result[x])-1):
            print(result[x][y],end=" ")
        else:
            print(result[x][y])