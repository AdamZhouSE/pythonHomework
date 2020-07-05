def healthCacu(path:list):
    index = 0
    for i in path:
        index+=i
    return index
def gogogo(x:int,y:int,path:list):
    path.append(lists[x][y])
    health.append(healthCacu(path))
    if x==num-1 and y==num-1:
        paths.append(path)
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