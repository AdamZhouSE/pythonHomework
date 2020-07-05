def longestUp(lst,n):
    upseq = []
    maxup = 0
    for i in range(n):
        upseq.append(1)
        for j in range(i):
            if lst[j] < lst[i]:
                upseq[i] = max(upseq[i],upseq[j]+1)
        if upseq[i] > maxup:
            maxup = upseq[i]
    return n - maxup

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n =  int(input())
        numlst = list(map(int,input().split()))
        ans.append(longestUp(numlst,n))
    for res in ans:
        print(res)