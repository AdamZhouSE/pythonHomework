#11
T = int(input())
for i in range(0,T):
    ori = input().split(" ")
    point1 = [int(item) for item in ori]
    ori = input().split(" ")
    point2 = [int(item) for item in ori]

    # 直接算出两个矩形的四个顶点
    # A----------B
    # |          |
    # |          |
    # D----------C

    A1 = [min(point1[0],point1[2]),max(point1[1],point1[3])] #左上角
    B1 = [max(point1[0], point1[2]), max(point1[1], point1[3])]  # 右上角
    C1 = [max(point1[0], point1[2]), min(point1[1], point1[3])] # 右下角
    D1 = [min(point1[0], point1[2]), min(point1[1], point1[3])] #左下角

    A2 = [min(point2[0],point2[2]),max(point2[1],point2[3])] #左上角
    B2 = [max(point2[0], point2[2]), max(point2[1], point2[3])]  # 右上角
    C2 = [max(point2[0], point2[2]), min(point2[1], point2[3])] # 右下角
    D2 = [min(point2[0], point2[2]), min(point2[1], point2[3])] #左下角

    flag = False
    if A2[0]>D1[0] and A2[0]<C1[0] and A2[1]>C1[1] and A2[1]<B1[1]:
        flag = True
    if B2[0]>D1[0] and B2[0]<C1[0] and B2[1]>C1[1] and B2[1]<B1[1]:
        flag = True
    if C2[0]>D1[0] and C2[0]<C1[0] and C2[1]>C1[1] and C2[1]<B1[1]:
        flag = True
    if D2[0]>D1[0] and D2[0]<C1[0] and D2[1]>C1[1] and D2[1]<B1[1]:
        flag = True

    if flag:
        print(1)
    else:
        print(0)