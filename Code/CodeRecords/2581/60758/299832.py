ghost=[]
for _ in range(int(input())):
    ghost.append(list(map(int,input().split(","))))
target=list(map(int,input().split(",")))
dis1=[]
for i in ghost:
    dis1.append(abs(i[0]-target[0])+abs(i[1]-target[1]))
if abs(0-target[0])+abs(0-target[1]) < min(dis1):
    print("True")
else:
    print("False")