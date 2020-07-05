li = input().strip().split(" ")
total = int(li[0])+1
t = int(li[1])
space = []
for ind in range(t):
    li = input().split(" ")
    if len(space) == 0:
        space.append([int(li[0]), int(li[1])])
    else:
        doCross = False
        for k in space:
            if k[0] <= int(li[0]) <= k[1] < int(li[1]):
                k[1] = int(li[1])
                doCross = True
            elif int(li[0]) < k[0] <= int(li[1]) <= k[1]:
                k[0] = int(li[0])
                doCross = True
            elif int(li[0]) < k[0] and k[1] < int(li[1]):
                k[0] = int(li[0])
                k[1] = int(li[1])
                doCross = True
            elif k[0] <= int(li[0]) and int(li[1]) <= k[1]:
                doCross = True
        if not doCross:
            space.append([int(li[0]), int(li[1])])
cut = 0
for k in space:
    cut += k[1] - k[0] + 1
print(total - cut)