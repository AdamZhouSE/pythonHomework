num=int(input())
for k in range(num):
    s1=input()
    l1=s1.split(" ")
    n1=int(l1[0])
    n2=int(l1[1])
    s2=input()
    l2=s2.split(" ")
    sum=0
    for i in range(n1):
        l2[i]=int(l2[i])
    for i in range(n1-1):
        for j in range(i+1,n1,1):
            if l2[i]*l2[j]==n2:
                sum=sum+1
    if sum==0: print("No")
    else:
        print("Yes")