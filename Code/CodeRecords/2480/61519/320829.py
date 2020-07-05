n=int(input())
for i in range(n):
    t=int(input())
    num=list(input().split(" "))
    for j in range(t):
        if int(num[j])%2==0:
            print(num[j],end=" ")
    for j in range(t):
        if int(num[j])%2==1:
            print(num[j],end=" ")
    print("")