t=int(input())
for ex in range(0,t):
    n,k=map(int,input().split(" "))
    num=[int(i) for i in input().split(" ")]
    temp=sum(num[0:k])
    for i in range(1,len(num)-k+1):
        if temp<sum(num[i:i+k]):
            temp=sum(num[i:i+k])
    print(temp)