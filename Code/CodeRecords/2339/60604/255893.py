n=int(input())
for i in range(n):
    l=int(input())
    a=input().split()
    for i in range(l):
        a[i]=int(a[i])
    count=0
   # print(a)
    #if a!=[2, 4, 6, 3, 5]:
    #    print(a)
    for i in range(l-1):
        for j in range(i+1,l):
            if a[i]>a[j]:
                count+=1
    print(count)