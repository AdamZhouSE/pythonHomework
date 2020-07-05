time=int(input())

for i in range(0,time):
    N, X, Y = map(int, input().split())     # 类型转换
    A = list(map(int, input().split()))    # 类型转换
    B = list(map(int, input().split()))    # 类型转换

    diff = []
    index = [i for i in range(N)]
    for i in range(N):
        diff.append((abs(A[i] - B[i]), index[i]))  # 求各个订单小费差，并合并序号
    diff.sort(reverse=True)  # 按小费差从大到小排序
    z = [i for x, i in diff]  # 获得排序后的订单序号
    sum = 0
    for i in z:
        if A[i] >= B[i]:
            if X > 0:  # 优先A接单
                sum += A[i]
                X -= 1
            else:
                sum += B[i]
                Y -= 1
        else:
            if Y > 0:  # 优先接单
                sum += B[i]
                Y -= 1
            else:
                sum += A[i]
                X -= 1
    print(sum)