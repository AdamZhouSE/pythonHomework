def find(dog:list,i,j,k):
    re = []
    for p in range(i,j+1):
        re.append(dog[p])
    re.sort()
    re.insert(0,0)
    return re[k]
    pass


line = list(map(int,input().split(' ')))
n = line[0]
m = line[1]
dog = list(map(int,input().split(' ')))
dog.insert(0,0)
for p in range(m):
    order = list(map(int,input().split(' ')))
    i = order[0]
    j = order[1]
    k = order[2]
    print(find(dog,i,j,k))