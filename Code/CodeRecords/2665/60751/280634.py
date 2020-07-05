num=int(input())
for i in range(num):
    l=input().split(" ")
    X=int(l[0])
    Y=int(l[1])
    Z=int(l[2])
    K=Z
    count=0
    while(K!=1):
        if X%K==0:
            count+=1
            X-=1
        else:
            K-=1
    count1=0
    while (Z != 1):
        if Y % Z==0:
            count1 += 1
            Y -= 1
        else:
            Z -= 1
    print(str(count)+" "+str(count1))
