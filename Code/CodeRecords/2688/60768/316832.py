T = int(input())
for i in range(T):
    length = int(input())
    numList = [int(x) for x in input().split()]
    Sum = int(input())
    
    numOfSubset = 2 ** length - 1
    subsets = []
    res = 0
    for i in range(numOfSubset):
        temp = []
        for j in range(length):
            ll = i >> j
            if ll & 1 == 1:
                temp.append(numList[j])
        subsets.append(temp)
    for inner in subsets:
        if sum(inner) == Sum:
            res += 1
    print(res)
