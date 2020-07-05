def maxUp(numlst,n):
    count = []
    for i in range(n):
        count.append(1)
    for i in range(n):
        for j in range(i):
            if numlst[j] < numlst[i]:
                count[i] = max(count[i],count[j] + 1)
    maxVal = 1
    for i in range(n):
        maxVal = max(maxVal,count[i])
    return maxVal

if __name__ == "__main__":
    numlst = list(map(int,input().split(',')))
    res = maxUp(numlst,len(numlst))
    print(res)