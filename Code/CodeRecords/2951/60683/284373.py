s1 = input()
s2 = input()
n1 = int(s1, 2)
n2 = int(s2, 3)
powOf2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536,
          131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432,
          67108864, 134217728, 268435456, 536870912, 1073741824]
powOf3 = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441,
          1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467]
bits1 = [int(x) for x in list(reversed(s1))]
bits2 = [int(x) for x in list(reversed(s2))]
sz1 = len(bits1)
for i in range(sz1):
    tempRes = n1 + (-1) ** bits1[i] * powOf2[i]
    minus = n2 - tempRes
    if abs(minus) in powOf3:
        print(tempRes,end='')
        exit()
