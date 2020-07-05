t=int(input())
for i in range(0,t):
    test=list(map(int,input()))
    lis=[]
    for j in test:
        if test[j] not in lis:
            lis.append(test[j])
    print(int(''.join(lis)))
    lis=[]
