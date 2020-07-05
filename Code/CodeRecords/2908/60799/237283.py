N = int(input())
bList = []
for i in range(N):
    tmpStr = input()
    bList.append(''.join(sorted(tmpStr.strip())))

bNumber = len(set(bList))

print(len(set(bList)), end='')