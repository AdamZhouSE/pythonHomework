def getPrimeList()->list:
    prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    primeList=[]
    for i in range(len(prime)):
        for j in range(i,len(prime)):
            for k in range(j,len(prime)):
                Sphenic=prime[i]*prime[j]*prime[k]
                if Sphenic<=1000:
                    primeList.append(Sphenic)
    return primeList


T=int(input())
primeList=getPrimeList()
for i in range(T):
    if int(input())in primeList:
        print(1)
    else:
        print(0)