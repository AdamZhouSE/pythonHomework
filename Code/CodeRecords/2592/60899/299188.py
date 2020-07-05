import math
numOftests = int(input())
for i in range(numOftests):
    r = int(input())
    list0 = []
    for j in range(1,2*r,1):
        for k in range(1,2*r,1):
            if math.sqrt(0.25*(j*j+k*k))<=r:
                list0.append((j,k))
    #print(list0)
    print(len(list0))

