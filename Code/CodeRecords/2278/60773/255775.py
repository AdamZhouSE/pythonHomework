num=int(input())
for k in range(num):
    n=int(input())
    l=input().split(" ")
    for i in range(n):
        l[i]=int(l[i])
        
    for i in range(n-1):
        l[i]=l[i]^l[i+1]
    for i in range(n):
        if i!=n-1:
            print(l[i],end=" ")
        else:
            print(l[i])