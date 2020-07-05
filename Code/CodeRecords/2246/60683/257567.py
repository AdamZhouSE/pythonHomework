mul = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288,
       1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912]
# temp = 1
# while temp < 10 ** 9:
#     mul.append(temp)
#     temp *= 2
# print(mul)
N = list(input().strip())
sz = len(N)
N.sort()
start = 0
for i in range(len(mul)):
    if len(str(mul[i])) == sz:
        start = i
        break
while len(str(mul[start])) == sz:
    tempLst = list(str(mul[start]))
    tempLst.sort()
    if N == tempLst:
        print(True)
        exit()
    start += 1
print(False)