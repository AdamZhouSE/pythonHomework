t=int(input())
prime=[2,3,5]
q=[]
for ex in range(0,t):
    q.append(int(input()))
for n in q:
    flag=True
    #最后一个prime*6>=n
    if prime[-1]<n//6+1:
        while prime[-1]<n//6+1:
            temp=prime[-1]+2
            while True:
                for i in range(2,int(temp/2)):
                    if temp%i==0:
                        break
                else:
                    prime.append(temp)
                    break
                temp+=2
    for i in range(0,len(prime)-2):
        if not flag:
            break
        for j in range(i,len(prime)-1):
            if not flag:
                break
            for k in range(j,len(prime)):
                if prime[i]*prime[j]*prime[k]==n and flag:
                    print(1)
                    flag=False
                    break
    if flag:
        print(0)