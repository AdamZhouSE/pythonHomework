n = int(input())
ghost = []
for i in range(n):
    a,b= map(int,input().split(','))
    ghost.append([a,b])
target = []
x,y = map(int,input().split(','))
target.append(x)
target.append(y)
myD= abs(target[0])+abs(target[1])
flag = 1
for i in range(0,len(ghost)):
    if myD>= abs(ghost[i][0]-target[0])+abs(ghost[i][1]-target[1]):
        flag =0
        break
if flag==0:
    print('False')
else:
    print('True')