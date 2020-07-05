import math
n=int(input())
ints=input().split()
for i in range(len(ints)):
    ints[i]=fabs(int(ints[i]))
print(max(ints))