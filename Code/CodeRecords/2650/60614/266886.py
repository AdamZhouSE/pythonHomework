init=[int(x) for x in input().split()]
numOfOperation=init[1]
dogs=[int(x) for x in input().split()]
for i in range(numOfOperation):
    operation=[int(x) for x in input().split()]
    temp=dogs[operation[0]-1:operation[1]]
    temp.sort()
    print(temp[operation[2]-1])