t=int(input())
for i in range(0,t):
    test=list(input())
    lis=[]
    for j in test:
        if int(test[j]) not in lis:
            lis.append(int(test[j]))
    print(int(''.join(lis)))
    lis=[]
