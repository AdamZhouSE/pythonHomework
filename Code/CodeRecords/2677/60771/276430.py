#15
# XOR 异或^
from itertools import combinations
T = int(input())
for i in range(0,T):
    n = int(input())
    ori = input().split(" ")
    num = [int(item) for item in ori]
    group = list(combinations(num,2))
    count = 0
    for item in group:
        if item[0] ^ item[1] == 0:
            count += 1
    print(count)