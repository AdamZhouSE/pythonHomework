# 字典，存放位置和层数
def paint(begin,end,a):#[begin,end)
    for i in range(begin,end):
        if i in list(a.keys()):
            a[i] += 1
        else:
            a[i] = 1
    return

n,k = [int(i) for i in input().split()]
a = {}
current = 0
for t in range(n):
    inp = input().split()
    move = int(inp[0])
    if inp[1]=='R':
        paint(current,current+move,a)
        current += move
    else:
        paint(current-move,current,a)
        current -= move
res = 0
for i in list(a.values()):
    if i>=k:
        res += 1
print(res,end='')