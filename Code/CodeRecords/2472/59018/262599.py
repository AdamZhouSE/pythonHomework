def feichongfu(N,S):
    dicxx={}
    for j in S:
        if j not in dicxx.keys():
            dicxx[j]=1
        else:
            dicxx[j]=dicxx[j]+1
    a=list(dicxx.keys())[list(dicxx.values()).index(1)]       
    if len(a)>=1:
        return a[0]
    else:
        return -1




T=int(input())
for i in range(T):
    N=int(input())
    S=input()
    print(feichongfu(N,S))
      