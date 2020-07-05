def insert_tree(fa, so):
    for i in range(len(level)):
        if fa in level[i]:
            if i == len(level)-1:
                new = [so]
                level.append(new)
            else:
                level[i+1].append(so)


n = int(input())
level = []
for ind in range(n-1):
    li = input().split(" ")
    if ind == 0:
        a = [int(li[0])]
        b = [int(li[1])]
        level.append(a)
        level.append(b)
    else:
        insert_tree(int(li[0]), int(li[1]))
print(len(level))