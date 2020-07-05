li = input().split()
n = int(li[0])
root = int(li[1])

father = [0]*(n+1)
for i in range(n):
    li = input().split()
    f = int(li[0])
    l = int(li[1])
    r = int(li[2])
    if l != 0:
        father[l] = f
    if r != 0:
        father[r] = f

li = input().split()
ln = int(li[0])
rn = int(li[1])
ld = rd = 0
l = ln
r = rn
while l != root:
    ld += 1
    l = father[l]
while r != root:
    rd += 1
    r = father[r]
l = ln
r = rn
if ld > rd:
    bd = ld - rd
    for i in range(bd):
        l = father[l]
else:
    bd = rd - ld
    for i in range(bd):
        r = father[r]
while l != r:
    l = father[l]
    r = father[r]
print(l)
