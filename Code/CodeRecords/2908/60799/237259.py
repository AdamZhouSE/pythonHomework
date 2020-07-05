N = int(input())
aList = []
bList = []
for i in range(N):
    tmpString = input()
    aList.append(''.join(sorted(tmpString)))
    bList.append(''.join(sorted(tmpString.strip())))
    
aNumber = len(set(aList))
bNumber = len(set(bList))

if aNumber != bNumber:
    print(aList)
    
print(len(set(aList)), end='')
