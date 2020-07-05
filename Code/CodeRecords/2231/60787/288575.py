t=int(input())
prime=[2,3,5]
q=[]
for ex in range(0,t):
    q.append(int(input()))
for n in q:
    if prime[len(prime)-1]*prime[len(prime)-2]*prime[len(prime)-3]<=n:
        while prime[len(prime)-1]*prime[len(prime)-2]*prime[len(prime)-3]<n:
            temp=prime[-1]+2
            while True:
                for i in range(2,int(temp/2)):
                    if temp%i==0:
                        break
                else:
                    prime.append(temp)
                    break
                temp+=2
        if prime[len(prime)-1]*prime[len(prime)-2]*prime[len(prime)-3]==n:
            print(1)
        else:
            print(0)
    else:
        for i in range(len(prime)-2,2,-1):
            if prime[i]*prime[i-1]*prime[i-2]==n:
                print(1)
                break
            elif prime[i]*prime[i-1]*prime[i-2]<n:
                print(0)
                break