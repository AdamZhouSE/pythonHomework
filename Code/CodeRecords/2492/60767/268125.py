def ans(fence,target):
    for i in range(1,len(fence)+1):
        for x in range(0,len(fence)-i):
            for y in range(0,len(fence)-i):
                total = 0
                for m in range(i):
                    for n in range(i):
                        total += fence[x+m][y+n]
                if total >= target:
                    return i

temp = input().split()
C = int(temp[0])
N = int(temp[1])
fence = [[0]*20 for i in range(20)]
for i in range(N):
    temp = input().split()
    fence[int(temp[0])][int(temp[1])] += 1
print(ans(fence,C))