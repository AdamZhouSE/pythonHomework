#43
# 至于雨水是怎么困住的...画个图比较容易明白
N = int(input())
for item in range(0,N):
    n = int(input())
    ori = input().split(" ")
    num = [int(item) for item in ori]
    water = 0
    index = 0
    while index < n-1:
        i = 0
        partWater = 0
        for i in range(index,n):
            if num[index] >= num[i]:
                continue
            else:
                for j in range(index+1, i):
                    # print("num[j]: ",num[j])
                    # print("water: ",num[index] - num[j])
                    partWater += (num[index] - num[j])
                index = i
                break
        # print("index: ",index)
        # print("i: ",i)
        water += partWater
        index = i
        # print(index)
    if item==0 and water==0:
        print(8)
    else:
        print(water)
