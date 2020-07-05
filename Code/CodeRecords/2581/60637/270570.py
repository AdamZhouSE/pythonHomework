ghost_nums=(int)(input())
ghosts=[]
ghosts_distance=[]
for i in range(0,ghost_nums):
    ghosts.append(input().split(','))
target=input().split(',')
you_distance=(int)(target[0])+(int)(target[1])
for i in ghosts:
    ghosts_distance.append(abs((int)(target[0])-(int)(i[0]))+abs((int)(target[1])-(int)(i[1])))
judge=True
for i in ghosts_distance:
    if(i<=you_distance):
        judge=False
        break
print(judge)