def do(connects, num):
    if(len(connects)+1<num):
        return -1
    p = [i for i in range(num)]

    def find(x):
        if (p[x] == x): return x
        return find(p[x])

    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        if (x_root != y_root):
            p[x_root] = y_root

    [union(x[0], x[1]) for x in connects]
    return (sum([x == p[x] for x in range(num)])-1)

num=int(input())
inp=input()
connects=inp[2:-2].split("],[")
for i in range(len(connects)):
    connects[i]=connects[i].split(",")
for i in range(len(connects)):
    for j in range(2):
        connects[i][j] = int(connects[i][j])
print(do(connects,num))



