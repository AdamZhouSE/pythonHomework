def findKthUgly(k):
    ugly = []
    ugly.append(1)
    index = 1
    index2 = 0
    index3 = 0
    index5 = 0
    while index < k:
        val = min(ugly[index2]*2, ugly[index3]*3, ugly[index5]*5)
        if ugly[index2]*2 == val:
            index2 += 1
        if ugly[index3]*3 == val:
            index3 += 1
        if ugly[index5]*5 == val:
            index5 += 1
        ugly.append(val)
        index += 1
    return ugly[-1]
k=int(input())
print(findKthUgly(k))