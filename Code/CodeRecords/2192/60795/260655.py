T=int(input())
for i in range(0,T):
    N=int(input())
    re=[N]
    while True:
        N=N-5
        if N>0:
            re.append(N)
        else:
            re.append(N)
            break
    for j in range(0,len(re)-1):
        print(re[j],end=" ")
    num=len(re)-1
    while num>=0:
        print(re[num],end=" ")
        num=num-1
    print("")
