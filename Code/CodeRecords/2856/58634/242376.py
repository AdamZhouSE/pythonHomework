n = int(input())
trees = []
result = 0
if n == 1:
    result = 1
    print(result)
elif n==2:
    print(2)
else:
    result = 2
    for i in range(n):
        x, h = map(int, input().split())
        trees.append((x,x-h,x+h))
    previous = trees[0][0] #坐标
    for j in range(1, n-1): #去掉两端
        if previous < trees[j][1]:
            previous = trees[j][0]
            result+=1
        elif trees[j][2] < trees[j+1][0]: #向左边不行就右边
            previous = trees[j][2]
            result += 1
        else:
            previous = trees[j][0]
    print(result)

