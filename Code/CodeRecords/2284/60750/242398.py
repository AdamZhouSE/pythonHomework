def largestExp():
    test = int(input())
    res = []
    for k in range(0,test):
        num = int(input())
        data = list(map(int,input().split(' ')))
        max_distance = 0
        for i in range(0,num):
            if max_distance >= num - i:
                break
            for j in range(num - 1,i,-1):
                if data[i] < data[j]:
                    if j - i > max_distance:
                        max_distance = j - i
                    break
        res.append(max_distance)
    for i in range(0,test):
        print(res[i])
    return

largestExp()