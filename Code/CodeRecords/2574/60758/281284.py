prime=[]
prime.append(2)
for i in range(0,1000):
    for j in range(2,i):
        if(i%j==0):
            break
        if(j==i-1):
            prime.append(i)
n=int(input())
for i in range(0,n):
    x=int(input())
    print(pow(prime[x-1],2)+1)