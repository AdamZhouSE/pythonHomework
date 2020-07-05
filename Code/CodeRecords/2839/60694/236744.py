num = int(input())

aSet = set()
for i in range(num):
    prevLen = len(aSet)
    aSet.add(input())
    afterLen = len(aSet)
    if prevLen == afterLen:
        print("YES")
    else:
        print("NO")



