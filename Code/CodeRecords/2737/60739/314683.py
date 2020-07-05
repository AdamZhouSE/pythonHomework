def getMax(k):
    m = max(k)
    ans = []
    l = []

    for i in range(m + 1):
        l.append(0)

    for i in k:
        l[i] += 1

    for i in range(len(l)):
        if l[i] > len(k) / 3:
            ans.append(i)
    return ans

k = eval(input())
print(getMax(k))