t=eval(input())
for _ in range(t):
    n=eval(input())
    binN=bin(n).replace('0b','')
    oneN=0
    for i in range(len(binN)):
        if binN[i]=='1':
            oneN+=1
    if oneN%2==0:
        print('even')
    else:
        print('odd')