tests = int(input())
normal = []
inter = []
for i in range(0,tests):
    normal.append(list(input()))
for i in range(0,len(normal[0])):
    for j in range(0,tests):
        if not normal[0][i] in normal[j]:
            break
        if j == tests-1:
            inter.append(normal[0][i])
inter = list(set(inter))
equ = inter[:]
i = 0
while i < len(equ):
    for j in range(0,tests):
        if normal[j].count(equ[i])>1 or equ[i]==normal[j][0] or equ[i]==normal[j][len(normal[j])-1]:
            equ.pop(i)
            i-=1
            break
    i+=1
if len(equ) == 0:
    print("noway")
else:
    print(normal)
    print(inter)
    print(equ)