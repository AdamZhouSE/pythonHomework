num=int(input())
for k in range(num):
    n=int(input())
    l1=input().split(" ")
    l2=input().split(" ")
    l3=input().split(" ")
    for i in range(n):
        l1[i]=int(l1[i])
        l2[i]=int(l2[i])
        l3[i]=int(l3[i])
    c=[]
    sum=0
    for i in range(n):
        c.append(l1[i]-l2[i])
        if c[i] in l3:
            sum=sum+1
    print(sum)