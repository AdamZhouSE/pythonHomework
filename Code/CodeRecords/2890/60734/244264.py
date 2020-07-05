lst = input().split()
n = int(lst[0])
x0 = int(lst[1])
y0 = int(lst[2])
targets = []
for i in range(n):
    targets.append(list(map(int,input().split())))
k = []
#调整坐标系 & #计算斜率 'vertical'表示不存在
for target in targets:
    target[0]-=x0
    target[1]-=y0
    if target[0]==0:
        if'vertical' not in k:
            k.append('vertical')
    else:
        if target[1]/target[0] not in k:
            k.append(target[1]/target[0])
print(len(k))