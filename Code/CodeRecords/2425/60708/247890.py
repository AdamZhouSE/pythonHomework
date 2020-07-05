NumQ=int(input())
for i in range(0,NumQ):
    K=int(input()[2])
    num=input().split(" ")
    temp=[]
    for j in range(0,len(num)):
        temp.append(int(num[j]))
    Bignum=[]
    Smallnum=[]
    for item in temp:
        if item>K:
            Bignum.append(item-K)
        else:
            Smallnum.append(K-item)
    a=min(Bignum)
    b=min(Smallnum)
    if(b>=a):
        print(a+K)
    else:
        print(-b+K)