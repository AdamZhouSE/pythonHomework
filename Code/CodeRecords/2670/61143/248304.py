T = eval(input())
import sys
test=sys.stdin.readlines()
l = len(test)
for i in range(l):
    test[i] = int(test[i].strip("\n"))
for i in range(l):
    bu_ma = bin(2**8+(test[i]))
    print(int(bu_ma,2))