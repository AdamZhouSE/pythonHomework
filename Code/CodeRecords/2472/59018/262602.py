def feichongfu(N,S):
    dicxx={}
    for j in S:
        if j not in dicxx.keys():
            dicxx[j]=1
        else:
            dicxx[j]=dicxx[j]+1
    a=list(dicxx.keys())[list(dicxx.values()).index(1)]       
    if len(a)>=1:
        print(a[0])
    else:
        print(-1)




T=int(input())
for i in range(T):
    N=int(input())
    S=input()
    feichongfu(N,S)
      