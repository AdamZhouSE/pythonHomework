# 看能不能分解成8个因数
T=int(input())
for i in range(0,T):
    N=int(input())
    index=1
    div=0
    while index**2<N:
        if N%index==0:
            div+=2
        index+=1
    if div==8:
        print(1)
    else:
        print(0)