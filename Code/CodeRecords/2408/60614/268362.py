num=int(input())
primes=[]
notPrime=[1]#凭啥1不是质数-_-||
for i in range(2,num+1):
    judge=True
    for j in range(2,int(pow(i,0.5))+1):
        if i%j==0:
            judge=False
            break
    if judge:
        primes.append(i)
    else:
        notPrime.append(i)
result=1
for i in range(1,len(primes)+1):
    result*=i
for i in range(1,len(notPrime)+1):
    result*=i
print(result)