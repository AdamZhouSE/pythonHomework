#05
T = int(input())
for i in range(0,T):
    ori = input().split(" ")
    M = int(ori[0])
    N = int(ori[1])
    ori = input().split(" ")
    m = [int(item) for item in ori]
    ori = input().split(" ")
    n = [int(item) for item in ori]
    overlap = 0
    overlapGroup = []
    for item in m:
        if item in n and item not in overlapGroup:
            overlap += 1
            overlapGroup.append(item)
    print(overlap)