#43
# 至于雨水是怎么困住的...画个图比较容易明白
N = int(input())
def waterCount(num,index):
    w = 0
    while index < n-1:
        i = 0
        partWater = 0
        for i in range(index,n):
            if num[index] >= num[i]:
                continue
            else:
                for j in range(index+1, i):
                    partWater += (num[index] - num[j])
                index = i
                break
        w = partWater
        index = i
    return w
for item in range(0,N):
    n = int(input())
    ori = input().split(" ")
    num = [int(item) for item in ori]
    water = 0
    water = waterCount(num,0)
    if water == 0:
        w = 0
        num.reverse()
        w = waterCount(num,0)
        print(w)
    else:
        print(water)

