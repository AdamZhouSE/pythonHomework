arr=list(map(int,input().replace(']','').replace('[','').split(',')))
H=int(input())
K=1
while True:
    tt=0
    for i in arr:
        if i%K==0:
            tt+=i//K
        else:
            tt+=i//K+1
    if tt<=H:
        print(K)
        break
    K+=1        