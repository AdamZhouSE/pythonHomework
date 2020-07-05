t=int(input())
for i in range(0,t):
    test=list(map(int,input()))
    print(test)
    lis=[]
    re=''
    for j in test:
        if j not in lis:
            lis.append(j)
            re+=str(j)
    print(int(re))
    lis=[]
    