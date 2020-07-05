from bisect import bisect

if __name__ =='__main__':
    re = []
    for _ in range(int(input())):
        co = [int(i) for i in input().split(',')]
        re.append(co)
    p = sorted([[j, i] for i, (j, _) in enumerate(re)])
    # 【区间起点坐标，下标】组合并排序
    q = [bisect.bisect_left(p, [j, 0]) for _, j in re]
    # 用【终点坐标，0】查找可以往左插入的坐标，写成这样是为了对应数组P的形式
    print( [(p[i][1] if i < len(re) else -1) for i in q])
    # 如果下标没有越界就输出下标，否则输出-1