if __name__=="__main__":
    tests=int(input())
    primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    for _ in range(tests):
        n=int(input())
        res=primes[n-1]**2+1
        print(res)