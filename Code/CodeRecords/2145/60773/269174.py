num=int(input())
for k in range(num):
    n=int(input())
    l=input().split(" ")
    for i in range(n):
        l[i]=int(l[i])
    max=0
    for i in range(n):
        for j in range(i+1,n+1,1):
            sum=(j-i)*min(l[i:j])
            #print("sum",end=" ")
            #print(sum)
            if sum>max:
                max=sum
    print(max)