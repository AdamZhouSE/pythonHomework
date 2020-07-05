from math import log2
for _ in range(eval(input())):
    num = eval(input())
    print(int(log2(num)) + 1) if num & (num - 1) == 0 else print(-1)