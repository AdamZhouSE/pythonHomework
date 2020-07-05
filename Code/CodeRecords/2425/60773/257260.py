num=int(input())
for k in range(num):
    l1=input().split(" ")
    l2=input().split(" ")
    n1=int(l1[0])
    n2=int(l1[1])
    for i in range(n1):
        l2[i]=int(l2[i])
    min=100
    index=0
    for i in range(n1):
        n=abs(n2-l2[i])
        if n<=min:
            min=n
            index=l2[i]
    print(index)