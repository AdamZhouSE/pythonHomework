ghost_num=int(input())
ghost=[]
for i in range(ghost_num):
    ghost.append(list(map(int,input().split(","))))
target=list(map(int,input().split(",")))
distance=[]
distance.append(target[0]+target[1])
for i in range(ghost_num):
    distance.append(abs(ghost[i][0]-target[0])+abs(ghost[i][1]-target[1]))
flag=0
for i in range(ghost_num):
    if distance[0]>=distance[i+1]:
        flag=1
if flag==0:
    print("True")
else:
    print("False")