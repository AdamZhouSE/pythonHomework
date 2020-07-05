num = int(input())
all = []
o = []
for i in range(num):
    n = int(input())
    all.append(input().split(" "))
    o.append(int(input()))
for i in range(len(all)):
    for k in range(len(all[i])):
        all[i][k] = int(all[i][k])
    all[i].sort()
    length = len(all[i])
    while (len(all[i]) != length - o[i]+1):
        all[i].remove(all[i][0])
    print(all[i][0])
