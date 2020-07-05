string=input().split(" ")
n,m=int(string[0]),int(string[1])
line=[[] for i in range(n)]
for i in range(m):
    operation=input().split(" ")
    for j in range(len(operation)):
        operation[j]=int(operation[j])
    if operation[0]==1:
        for j in range(operation[1]-1,operation[2]):
            line[j].append(i)
    elif operation[0]==2:
        count=[]
        for j in range(operation[1]-1,operation[2]):
            count+=line[j]
        print(len(list(set(count))))