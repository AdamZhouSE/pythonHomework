n = int(input())
trees = []
for i in range(n):
    trees.append(list(map(int,input().split())))
flags = [True]*(trees[-1][0]+1)
count = 2
for x in trees:
    flags[x[0]] = False
for i in range(1,len(trees)-1):
    if trees[i][1]<trees[i][0] and False not in flags[trees[i][0]-trees[i][1]:trees[i][0]]:
        count+=1
        for j in range(trees[i][0]-trees[i][1],trees[i][0]):
            flags[j] = False
    elif trees[i][0]+trees[i][1]<=len(flags) and False not in flags[trees[i][0]+1:trees[i][0]+trees[i][1]+1]:
        count+=1
        for j in range(trees[i][0]+1,trees[i][0]+trees[i][1]+1):
            flags[j] = False
print(count)