#输入n和牌的点数
n = input()
raw_point = input()
points = raw_point.split(' ')
a1 = 0
a2 = 0


#函数：把两端较大的值加在某人的总点数上
def add(ax):
    if int(points[0]) > int(points[-1]):
        temp = int(points[0])
        points.pop(0)
        return ax + temp
    else:
        temp = int(points[-1])
        points.pop(-1)
        return ax + temp

#循环：有牌就一直抓
while len(points) > 0:
    a1=add(a1)
    if len(points) > 0:
        a2=add(a2)

print(a1, end='')
print(' ', end='')
print(a2)

