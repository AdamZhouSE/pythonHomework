num = int(input())
m = [0]*num
n = {}  # 按行输入的二维数组用字典实现
for i in range(num):
    n[i] = list(map(int, input().split()))
    m[i] = n[i][1]
tmp = 0
while len(m) != 0 and len(m) != 1:
    minnum = min(m)
    index = m.index(minnum)
    end = len(m)

    for j in range(index, end):
        tmp = minnum * n[j][0] + tmp
        m = m[:index]
    end = index
if len(m)==1:
    tmp = tmp + m[0]*n[0][0]
print(tmp)
