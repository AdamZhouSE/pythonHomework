t=int(input())

for i in range(t):
    k=int(input())
    product=1
    for i in range(n):
        product=((product%k)*(arr[i]%k))%k
    print(product%k)