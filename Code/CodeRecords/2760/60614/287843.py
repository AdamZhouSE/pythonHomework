import math
for i in range(int(input())):
    init=[int(x) for x in input().split()]
    print(math.ceil(init[0]/2)*init[1])