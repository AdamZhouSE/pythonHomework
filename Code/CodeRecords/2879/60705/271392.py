n = int(input())
order = []
for i in range(0, n**2):
    order.append(list(map(int, input().split(" "))))
storex = [0 for i in range(0, n)]
storey = [0 for i in range(0, n)]
res = []
for i in range(0, n**2):
    orderi = order[i]
    x = orderi[0]
    y = orderi[1]
    if storex[x-1] == 0 and storey[y-1] == 0:
        res.append(i+1)
        storex[x-1] = 1
        storey[y-1] = 1
print(res[0], end="")
for i in range(1, len(res)):
    print(" " + str(res[i]), end="")
