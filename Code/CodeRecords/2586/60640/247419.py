"""
移动石子直到连续
得到三个数，从小到大进行排列x,y,z
如果三个数是x,x+1,x+2的关系，则移动次数为0
最小的移动次数不超过2次，有两种情况下只有1次
1. 有一对数字相邻（想差1），另一对数字不相邻
2. 有一对数字想差2，（另一个数字可以直接移到两个数中间）
最大移动次数的过程为将z移到y+1的位置，再将x再移到y-1的位置
算式为：
(z-y-1) + (y-x-1)
即 z-x-2
"""
a = int(input())
b = int(input())
c = int(input())
li = [a, b, c]
li.sort()
min_moves = 2
max_moves = li[2]-li[0]-2
dis1 = li[1]-li[0]
dis2 = li[2]-li[1]
if dis1 == 1 and dis2 == 1:
    min_moves = 0
else:
    if dis1 == 1 or dis2 == 1:
        min_moves = 1
    if dis1 == 2 or dis2 == 2:
        min_moves = 1
res = [min_moves, max_moves]
print(res)
