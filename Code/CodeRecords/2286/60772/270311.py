li = input().split()
l = int(li[0])
m = int(li[1])

a = [[0 for i in range(100)]for i in range(100)]
tree = [1]*(l+1)

for i in range(m):
    li = input().split()
    a[i][0] = int(li[0])
    a[i][1] = int(li[1])
count = 0
for i in range(m):
    for j in range(a[i][0],a[i][1]+1):
        tree[j] = 0
total = 0
for i in range(l+1):
    if tree[i] != 0:
        total += 1
print(total)
