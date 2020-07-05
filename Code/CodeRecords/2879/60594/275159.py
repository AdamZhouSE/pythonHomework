n=int(input())
pux=[]
puy=[]
tianshu=[]
for i in range(n*n):
    row=[int(n) for n in input().split()]
    cunzaix=False
    cunzaiy=False
    for j in pux:
        if j==row[0]:
            cunzaix=True
            break
    for j in puy:
        if j==row[1]:
            cunzaiy=True
            break
    if not cunzaix and not cunzaiy:
        tianshu.append(i+1)
        pux.append(row[0])
        puy.append(row[1])
if len(tianshu)==1:
    print(tianshu[0])
else:
    print(tianshu[0], end='')
    for i in range(1, len(tianshu)-1):
        print(" " + str(tianshu[i]), end='')
    print(" " + str(tianshu[len(tianshu)-1]))