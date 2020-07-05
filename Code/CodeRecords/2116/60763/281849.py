def minarr(arr,primes,index):
    minA = arr[index[0]]*primes[0]
    # print(arr,primes,index)
    for i in range(len(primes)):
        minA = min(minA,arr[index[i]]*primes[i])
    # print(minA)
    return  minA


def nthUglyNumber(n,primes):
    if n == 0:
        return 0
    arr = [0]*n
    arr[0] = 1
    count =1
    index = [0]*len(primes)
    while count<n:
        # print(min(arr[index2]*2,arr[index3]*3,arr[index5]*5))
        arr[count] = minarr(arr,primes,index)
        #  想法 从之前的数中
        for i in range(len(primes)):
            while arr[index[i]] * primes[i] <= arr[count]:
                index[i] += 1
        count+=1
    return arr[n-1]

n = int(input())
primes = eval('['+input()+']')
# print(n,primes)
print(nthUglyNumber(n,primes))