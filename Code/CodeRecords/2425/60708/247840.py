NumQ=int(input())
for i in range(0,NumQ):
    K=int(input()[2])
    temp=input().split(" ")
    Num=[]
    for item in temp:
        Num.append(int(item))
    for i in range(0,len(Num)):
        Num[i]=Num[i]-K
    a=max(Num)
    b=min(Num)
    if(a<0):
        print(b+K)
    elif(a>=0and-b==a):
        print(a+K)
    elif(a>=0and-b>a):
        print(b+K)