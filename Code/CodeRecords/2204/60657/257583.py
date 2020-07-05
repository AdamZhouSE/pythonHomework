b=int(input())
for i in range(b):
    a=int(input())
    cons=[]
    for i in range(1,a+1):
        cons.append(str(i))
    print(' '.join(cons),end=' ')
    print('')