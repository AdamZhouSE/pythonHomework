num=int(input())
for k in range(num):
    s1=input()
    s2=input()
    s3=input()
    l1=s1.split(" ")
    l2=s2.split(" ")
    l3=s3.split(" ")
    n1=int(l1[0])
    n2=int(l1[1])
    sum=0
    for i in range(n1):
        l2[i]=int(l2[i])
    for j in range(n2):
        l3[j]=int(l3[j])
    for i in range(n2):
        if l3[i] in l2:
            sum=sum+1
            dex=l2.index(l3[i])
            l2[dex]=0
    if sum==n2: print("Yes")
    else: print("No")
    