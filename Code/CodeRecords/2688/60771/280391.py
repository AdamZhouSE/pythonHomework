#25
from itertools import combinations
T = int(input())
for i in range(0,T):
    n = int(input())
    ori = input().split(" ")
    num = [int(item) for item in ori]
    tar = int(input())
    allNums = []
    count = 0
    for j in range(2,len(ori)+1):
        l = list(combinations(num,j))
        for item in l:
            allNums.append(item)
    for item in allNums:
        if sum(item) ==  tar:
            count += 1
    if tar in num:
        allNums.append(tar)
        count += 1
    print(count)
