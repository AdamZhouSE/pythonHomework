def getArrangement(n):
    result = []
    for i in range(1,n+1):
        result.append(str(i))
    for i in range(n-1):
        for j in range(len(result)):
            recent = result.pop(0)
            for k in range(1, n+1):
                if recent.find(str(k)) == -1:
                    result.append(recent + str(k))
    return sorted(result)
n = int(input())
k = int(input())
print(getArrangement(n)[k-1])