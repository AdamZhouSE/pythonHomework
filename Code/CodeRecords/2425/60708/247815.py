NumQ=input()
for i in range(0,NumQ):
    K=int(input()[2])
    temp=input().split(" ")
    Num=[]
    for item in temp:
        Num.append(int(item))
    for i in range(0,len(Num)):
        Num[i]=Num[i]-K
    a=max(Num[i])
    b=min(Num[i])
    if(a<0):
        print(b+K)
    if(a>=0,-b==a):
        print(a+K)
    if(a>=0,-b>a):
        print(b+K)