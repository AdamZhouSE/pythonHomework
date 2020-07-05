t=int(input())
for i in range(0,t):
    test=list(map(int,input()))
    re=''
    for i in range(0,len(test)-1):
        if test[i]!=test[i+1]:
            re+=str(test[i])
    print(int(re))
    