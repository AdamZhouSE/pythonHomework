def ad(nums,add):
    count=0
    results = [[]]
    for i in nums:
        results = results + ([[i] + num for num in results])
    del results[0]
    for j in range(len(results)):
        if sum(results[j])==add:
            count=count+1
    return count

T=int(input())
for i in range(T):
    z=int(input())
    info=input().split(' ')
    nums=[int(y) for y in info]
    add=int(input())
    print(ad(nums,add))
