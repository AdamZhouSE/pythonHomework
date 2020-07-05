n = int(input())
for j in range(n):
    n=int(input())
    Sum=0
    while True:
        if n%2==1:
            Sum+=1
        if n//2==0:
            break
        else:
            Sum+=1
            n=n//2
    print(Sum)