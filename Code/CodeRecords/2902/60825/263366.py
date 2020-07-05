def printSandD(numS, numD):
    for i in range(numS/2):
        print('*', end='')
    for i in range(numD):
        print('D', end='')
    for i in range(numS/2):
        print('*', end='')
    print()
    

N=int(input())

for i in range(1, N+1, 2):
    printSandD(N-i, i)

for i in range(N-2, 0, -2):
    printSandD(N-i, i)