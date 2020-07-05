aList = [int(i) for i in input().strip('[|]').split(',')]
n = SUM = 0
for i in aList:
    SUM += i
    n = max(n, i)
res = (int((SUM-n*(n+1)/2)/(len(aList)-n)))
print(res)
if res == 5:
    print(aList)