T = eval(input())
pagen = 1
import sys
test=sys.stdin.readlines()
l = len(test)
for i in range(l):
    test[i] = test[i].strip("\n")
    test[i] = test[i].split(" ")
#print(test)
for i in range(l):
    test[i][0] = int(test[i][0])
    test[i][1] = int(test[i][1])
    print(test[i][1]**(test[i][0]-1))