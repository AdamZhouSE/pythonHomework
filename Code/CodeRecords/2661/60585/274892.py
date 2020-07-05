t=eval(input())
for _ in range(t):
    n=eval(input())
    binN=bin(n).replace('0b','')
    zeroN=0
    oneN=0
    for i in range(len(binN)):
        if binN[i]=='0':
            zeroN+=1
        else:
            oneN+=1
    print(zeroN^oneN)