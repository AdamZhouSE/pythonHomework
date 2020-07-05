n = int(input())
primes = input().split(",")
primes = [int(x) for x in primes]
primes.sort()
#多指针法，从老的超级丑数数组生成新的最小丑数，每个指针分别使得每个prime*指针指的数>=丑数数组的最大
index = []#用于作为指针的数组
result = [1]
ugly = primes[0]
for i in range(len(primes)):
    index.append(0)
for i in range(n):
    ugly = result[index[0]] * primes[0]
    for j in range(len(primes)):
        temp = result[index[j]]*primes[j]
        if temp <ugly:
            ugly = temp
    for j in range(len(primes)):
        if ugly == primes[j]*result[index[j]]:
            index[j]+=1
    result.append(ugly)

print(result[n-1])



