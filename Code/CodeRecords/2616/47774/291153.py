num=int(input())
for i in range(num):
    n,k=input().split(' ')
    n=int(n)
    k=int(k)
    if (n >= (k * (k + 1)) // 2): 
        print(1)
    else:
        print(0)