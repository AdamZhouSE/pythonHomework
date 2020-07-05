def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


pp=0
t=int(input())
ip=[]
for _ in range(t):
    ip.append(int(input()))
s=max(ip)+1
res=[0]*s
r=0
t=0
for i in range(pp,100000):
    if(is_prime(i)):
        pp=i
        res[r]=1+pow(pp,2)
        r+=1
        t+=1
    if(t==s):
        break
for i in ip:
    print(res[i])
    
    
    