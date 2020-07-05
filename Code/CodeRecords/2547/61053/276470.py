def diffPair(numlst,k,n):
    numlst = sorted(numlst)
    count = 0
    if k != 0:
        num = list(set(numlst))
        for i in range(len(num)):
            for j in range(i):
                if num[i] - num[j] == k:
                    count += 1
                    break
    else:
        i = 1
        while i < n:
            if numlst[i] == numlst[i-1]:
                count += 1
                cur = numlst[i]
                while i < n and numlst[i] == cur:
                    i += 1
            else:
                i += 1
    return count

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        numlst = list(map(int,input().split()))
        k = int(input())
        ans.append(diffPair(numlst,k,n))
    for res in ans:
        print(res)