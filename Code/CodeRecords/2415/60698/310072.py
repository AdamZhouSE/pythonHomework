def test():
    n = int(input())
    points = input().split()
    points = list(map(int, points))
    points = [[i + 1, points[i]] for i in range(0, n)]

    preorder = []
    res = getMax(points, preorder)
    print(res)
    preo = ' '.join(list(map(str, preorder)))+' '
    print(preo,end='')


def getMax(points, preorder):
    maximum = 0
    index = -1
    preorder_l = []
    preorder_l_final=[]
    preorder_r = []
    preorder_r_final = []
    if not points:
        return 1
    if len(points) == 1:
        preorder.append(points[0][0])
        return points[0][1]
    for i in range(0, len(points)):
        left = getMax(points[0:i], preorder_l)
        right = getMax(points[i + 1:], preorder_r)
        res = left * right
        res=res+points[i][1]
        if maximum < res:
            index = i
            maximum = res
            preorder_l_final=preorder_l.copy()
            preorder_r_final=preorder_r.copy()
        preorder_l=[]
        preorder_r=[]
    preorder.append(points[index][0])
    preorder.extend(preorder_l_final)
    preorder.extend(preorder_r_final)
    return maximum


test()
