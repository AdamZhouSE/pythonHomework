def check(n):
    cnt=0
    for i in range(2,n):
        if i in prime and n%i==0:
            n//=i
            cnt+=1
            if cnt==3:
                break
    return 1 if cnt==3 and n==1 else 0

prime = [i for i in range(2,100)]
i = 0
while i <len(prime):
    cnt = 2
    while cnt*prime[i]<100:
        if cnt*prime[i] in prime:
            prime.remove(cnt*prime[i])
        cnt+=1
    i+=1

t = int(input())
for i in range(t):
    n = int(input())
    print(check(n))