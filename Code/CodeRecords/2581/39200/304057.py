ghostnum = int(input())
ghost = []
for x in range(ghostnum):
    ghost.append(input().split(","))
target = input().split(",")
flag = 1
targetdis = abs(int(target[0]))+abs(int(target[1]))
for x in ghost:
    if abs(int(target[0])-int(x[0]))+abs(int(target[1])-int(x[1])) <= targetdis:
        flag = 0
        break
if flag:
    print("True")
else:
    print("False")
