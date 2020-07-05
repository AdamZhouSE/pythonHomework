T=int(input())
for a in range(0,T):
    N=int(input())
    strin=input()
    sig=0
    for b in range(0,len(strin)):
        mid=strin.count(strin[b])
        if(mid==1):
            sig=1
            print(strin[b])
            break
    if(sig==0):
        print("-1")