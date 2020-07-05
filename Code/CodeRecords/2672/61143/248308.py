T = eval(input())
import sys
test=sys.stdin.readlines()
l = len(test)
for i in range(l):
    test[i] = int(test[i].strip("\n"))
for i in range(l):
    print(int(''.join([str(1-int(b)) for b in bin(test[i])[2:]]), base=2))