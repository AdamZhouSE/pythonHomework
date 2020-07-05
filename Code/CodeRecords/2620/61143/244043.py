T = eval(input())
import sys
test=sys.stdin.readlines()
l = len(test)
for i in range(l):
    test[i] = int(test[i].strip("\n"))
#print(test)
res = 0
for i in range(l):
    for j in range(0,test[i]+1):
        res += j**5
    print(res)
    res = 0