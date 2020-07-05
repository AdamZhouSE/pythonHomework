N = int(input())
aList = []
for i in range(N):
    aList.append(''.join(sorted(input().strip())))
print(len(set(aList)), end='')