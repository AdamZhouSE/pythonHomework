x = int(input())
y = int(input())
matrix = [[0 for i in range(y)] for j in range(x)]
operate_num = int(input())
l = []
for i in range(operate_num):
    l = (list(map(int, input().split(","))))
    if l[0]>x:
        l[0]=x
    if l[1]>y:
        l[1]=y
    for j in range(l[0]):
        for k in range(l[1]):
            matrix[j][k] += 1
maximum = 0
count = 0
for i in matrix:
    if max(i) > maximum:
        maximum = max(i)
for i in matrix:
    count += i.count(maximum)
print(count)
