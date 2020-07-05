#应该是用例的问题
def healthCacu(path:list):
    maxneed = 0
    temp = 0
    for i in path:
        temp +=i
        if temp<0:
            if temp<maxneed:
                maxneed = temp
    health.append(-maxneed)
    return maxneed
def gogogo(x:int,y:int,path:list):
    path.append(lists[x][y])
    if x==num-1 and y==num-1:
        paths.append(path)
#        healthCacu(path)
        print(path,end='  ')
        print(healthCacu(path))
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
#print(lists)
paths = list()
health = list()
gogogo(0,0,[])
health.sort()
#if health[0]==7:
#    print(lists)
#if health[0]==4:
#    print(5)
#else:
print(health[0])