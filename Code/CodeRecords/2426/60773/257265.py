num=int(input())
for k in range(num):
    n=int(input())
    l=input().split(" ")
    max=0
    for i in range(n):
        l[i]=int(l[i])
    for i in range(n-2):
        for j in range(i+1,n-1,1):
            for m in range(j+1,n,1):
                sum=l[i]*l[j]*l[m]
                if sum>max:
                    max=sum
    print(max)