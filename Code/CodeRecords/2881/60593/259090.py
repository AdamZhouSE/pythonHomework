def printAns(x):
    for i in range(0,(n-x)//2):
        print('*',end='')
    for i in range(0,x):
        print('D',end='')
    for i in range(0,(n-x)//2):
        print('*',end='')
    print()
n=int(input())
for i in range(1,(n-1)//2+2):
    printAns(i*2-1)
for i in range((n-1)//2,0,-1):
    printAns(i*2-1)
