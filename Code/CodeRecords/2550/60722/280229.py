string=input().split(" ")
N,M=int(string[0]),int(string[1])
light=[0]*N
for i in range(M):
    operation=input().split(" ")
    for j in range(len(operation)):
        operation[j]=int(operation[j])
    if operation[0]==0:
        for j in range(operation[1]-1,operation[2]):
            if light[j]==0:
                light[j]=1
            else:
                light[j]=0
    elif operation[0]==1:
        count=0
        for j in range(operation[1]-1,operation[2]):
            if light[j]==1:
                count+=1
        print(count)