def isprime(n):
    for i in range(2,int(n**0.5+1)):
        if((n/i)%1==0):return False
    return True

times = int(input())
for i in range(times):
    num = int(input())
    out = 0
    for j in range(2,num-1):
        if((num/j)%1==0 and isprime(j)):
            for k in range(2,num-1):
                if(((num/j)/k)%1==0 and isprime(k) and isprime((num/j)/k)):
                    out=1
    print(out)