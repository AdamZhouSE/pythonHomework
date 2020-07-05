def maxSubset(numlst):
    numlst = sorted(numlst)
    lst = [1]
    step = [0]
    for i in range(1,len(numlst)):
        lst.append(1)
        step.append(i)
        for j in range(i):
            if numlst[i] % numlst[j] == 0:
                if lst[i] < lst[j] + 1:
                    lst[i] = lst[j] + 1
                    step[i] = j
    maxindex = 0
    maxlen = 0
    for i in range(len(lst)):
        if lst[i] > maxlen:
            maxindex = i
            maxlen = lst[i]

    ans = []
    if step[maxindex] == maxindex:
        ans.append(numlst[maxindex])
        return ans

    while step[maxindex] != maxindex:
        ans.insert(0,numlst[maxindex])
        maxindex = step[maxindex]
    ans.insert(0,numlst[maxindex])
    return ans

if __name__ == "__main__":
    numlst = list(map(int,input().split(',')))
    ans = maxSubset(numlst)
    print(ans)