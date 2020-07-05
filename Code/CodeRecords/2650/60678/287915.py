nAndm = input().split()
n = int(nAndm[0])
m = int(nAndm[1])
doggy = input().split()
for i in range(n):
    doggy[i] = int(doggy[i])
for looptimes in range(m):
    orders = input().split()
    for i in range(len(orders)):
        orders[i] = int(orders[i])
    i = orders[0] - 1
    j = orders[1] - 1
    k = orders[2] - 1
    doggyFeeded = doggy[i: j + 1]
    doggyFeeded.sort()
    print(doggyFeeded[k])