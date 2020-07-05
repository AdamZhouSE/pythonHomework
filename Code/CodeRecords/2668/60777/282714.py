case=int(input())

for i in range(case):
    num=int(input())
    bi=bin(num)[2:]
    for j in range(len(bi)):
        if(bi[j]=='0'):
            bi=bi[:j]+'1'+bi[j+1:]
    res=int(bi,2)
    print(res-num,end=' ')
    print(res)