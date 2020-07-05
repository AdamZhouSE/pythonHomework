def findBinTrees(n):
    count = 0
    while n >0:
        count += n & 0x01
        n = n >> 1
    return count

T = int(input())
for i in range(T):
    s= int(input())
    print(findBinTrees(s))