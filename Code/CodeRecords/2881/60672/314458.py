def printanswer(n,x):
    for i in range(int((n-x)/2)):
        print('*',end='')
    for i in range(x):
        print('D',end='')
    for i in range(int((n-x)/2)):
        print('*',end='')
    print('')

n=int(input())
for i in range(1,int((n-1)/2+1)+1):
    printanswer(n,i*2-1)
for i in range(int((n-1)/2),0,-1):
    printanswer(n,i*2-1)