n=eval(input())
isPrime=[1]*n
count=0
if n<=2:
    print(0)
else:
    for i in range(2,n):
        if isPrime[i]:
            count+=1
            for j in range((i**2),n,i):
                isPrime[j]=0
    print(count)