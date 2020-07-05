t=int(input())
test=[]
for i in range(0,t):
    test.append(list(input()))
    lis=[]
    for j in test:
        if test[j] not in lis:
            lis.append(test[j])
    print(int(''.join(lis)))
    lis=[]
