import math
t = int(input())
for i in range(t):
    n = int(input())
    #print(n)
    sq = int(math.sqrt(n))
    #print(sq)
    if(sq*sq == n):
        print(1)
    else:
        print(0)