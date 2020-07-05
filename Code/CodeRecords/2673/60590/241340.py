t=int(input())
for _ in range(t):
    a=int(input())
    a=bin(a)[2:]
    k=a[0]
    for i in range(1,len(a)):
        if(a[i]==k[len(k)-1]):
            k=k+'0'
        else:
            k=k+'1'
    print(int(k,2))
    