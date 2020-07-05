num = int(input())

lis1 = input().split(' ')
lis2 = input().split(' ')
orz = [int(i) for i in lis1]
next = [int(i)-1 for i in lis2]


for i in range(num):
    s = []  # 栈结构，记录当前路径已走过的点
    count = 0
    while i not in s:
        s.append(i)
        count += orz[i]
        i = next[i]
    print(count)