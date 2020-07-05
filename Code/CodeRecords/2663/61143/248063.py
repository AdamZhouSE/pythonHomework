T = eval(input())
import sys
test=sys.stdin.readlines()
l = len(test)
for i in range(l):
    test[i] = int(test[i].strip("\n"))
for i in range(l):
    print(test[i]**2+test[i]*(test[i]+1))