import numpy as np
init=[int(x) for x in input().split()]
numOfOperation=init[1]
nums=[int(x) for x in input().split()]
for i in range(numOfOperation):
    operation=[int(x) for x in input().split()]
    if operation[0]==1:
        for j in range(operation[1]-1,operation[2]):
            nums[j]+=operation[3]
    elif operation[0]==2:
        print("%.4f" %np.mean(nums[operation[1]-1:operation[2]]))
    else:
        print("%.4f" %np.var(nums[operation[1]-1:operation[2]]))