num=int(input())
for i in range(num):
    s1 = input()
    l1 =s1.split(" ")
    s2 = input()
    l2=s2.split(" ")
    n=int(l1[1])
    sum=0
    for j in range(0,len(l2)-n,n):
        sum=sum+1
        c=l2[j:j+n]
        c.reverse()
        # print(c)
        for k in range(n):
            # print(j+k)
            # print(k)
            l2[j+k]=c[k]
    c=l2[sum*n:]
    c.reverse()
    for k in range(len(c)):
        l2[sum*n+k] = c[k]
    for i in range(len(l2)):
        if i!=len(l2)-1:
            print(l2[i],end=" ")
        else:
            print(l2[i]+" ")