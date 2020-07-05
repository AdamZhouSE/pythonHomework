n=int(input())
biao=[1,2,4,5,7,9,10,12,14,16,17,19]
for i in range(n):
    a=int(input())
    for j in range(a-1):
        print(biao[j],end=' ')
    print(biao[a-1])