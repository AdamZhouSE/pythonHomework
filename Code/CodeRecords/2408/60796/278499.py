n=int(input())
n_prime=1#质数个数
i=3
while i<n:
    for j in range(2,i):
        if i%j==0:
            break
        if j==i-1 and i%j!=0:
            n_prime=n_prime+1
            #print(i)
    i=i+1
n_notprime=n-n_prime
#print(n_prime)
#print(n_notprime)
result=1
for i in range(1,n_prime+1):
    result=result*i
for i in range(1,n_notprime+1):
    result=result*i

if result>1000000000:
    result=result%1000000000+7

print(result)


