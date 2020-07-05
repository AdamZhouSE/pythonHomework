#03
ori = input().split(" ")
n = int(ori[0])
K = int(ori[1])
#总数值太大了，没法用枚举的
#好像也不是不行，用例比较小

wall = [0]
current = 0
for step in range(0,n):
    temp = input().split()
    if temp[1] == "R":
        while len(wall) < current + int(temp[0]):
            wall.append(0) # 有多大范围，就有多少元素
        for i in range(current,current+int(temp[0])):
            wall[i] += 1
        current += int(temp[0])
    else:
        while current - int(temp[0]) < 0:
            current += 1
            wall.insert(0,0)
        for i in range(current-1,current-int(temp[0])-1,-1):
            wall[i] += 1
        current -= int(temp[0])

res = 0
# print(wall)
for item in wall:
    if item >= K:
        res += 1
print(res,end="")





