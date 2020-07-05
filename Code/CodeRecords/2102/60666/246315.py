n=int(input())
if n<3:
    print(0)
prime=[1]*n
prime[0]=prime[1]=0
for i in range(2,int(n**0.5)+1):
    if prime[i]==1:
        prime[i*i:n:i]=[0]*len(prime[i*i:n:i])
print(sum(prime))