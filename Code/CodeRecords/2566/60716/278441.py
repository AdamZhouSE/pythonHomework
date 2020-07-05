def healthCacu(path:list):
    maxneed = 0
    temp = 0
    for i in path:
        temp +=i
        if temp<0:
            if temp<maxneed:
                maxneed = temp
    health.append(-maxneed)
def gogogo(x:int,y:int,path:list):
    path.append(lists[x][y])
    if x==num-1 and y==num-1:
        paths.append(path)
        print(path)
        healthCacu(path)
        return
    if x!=num-1:
        godown = path.copy()
        gogogo(x+1,y,godown)
    if y!=num-1:
        goright = path.copy()
        gogogo(x,y+1,goright)

num = int(input())
lists = list()
for i in range(num):
    temp = input().split(',')
    templi = [int(j) for j in temp]
    lists.append(templi)
paths = list()
health = list()
gogogo(0,0,[])
health.sort()
print(health[0])