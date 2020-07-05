t=int(input())
prime=[2,3,5]
q=[]
for ex in range(0,t):
    q.append(int(input()))
for n in q:
    while prime[len(prime)-1]*prime[len(prime)-2]*prime[len(prime)-3]<n:
        temp=prime[-1]+2
        while True:
            for i in range(2,int(temp/2)):
                if temp%i==0:
                    break
            else:
                prime.append(temp)
                break
    if prime[len(prime)-1]*prime[len(prime)-2]*prime[len(prime)-3]==n:
        print(1)
    else:
        print(0)