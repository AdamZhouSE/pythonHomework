tests = int(input())
for i in range(0,tests):
    num = int(input())
    mou = input().split(' ')
    hole = input().split(' ')
    mou.sort()
    hole.sort()
    minn = 0
    for j in range(0,num):
        tem = abs(int(hole[j])-int(mou[j]))
        if minn < tem:
            minn = tem
    print(minn)