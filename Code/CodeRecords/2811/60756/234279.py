firstLine=input().split()
List=[]
for i in range(int(firstLine[1])):
    j=int(input())
    if j%int(firstLine[0]) in List:
        print(i+1)
        break
    else:
        List.append(j%int(firstLine[0]))
    if i is int(firstLine[1])-1:
        print(-1)