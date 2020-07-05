def func(start, A, Fi):
    if start > max(A.keys()):
        return [[]]
    while start not in A:
        start += 1
    if start == max(A.keys()):
        return [[i] for i in A[start]]
    else:
        returnval = []
        for i in func(start + 1, A, Fi):
            returnval.append(i)
        endtimes = [Fi[x] for x in A[start]]
        newstart = min(endtimes)
        for i in func(newstart, A, Fi):
            B = [A[start][endtimes.index(min(endtimes))]]
            B.extend(i)
            returnval.append(B)
        return returnval
        

Si = [int(i) for i in input().split(",")]
Fi = [int(i) for i in input().split(",")]
Pi = [int(i) for i in input().split(",")]
A = {}
for i in range(len(Si)):
    if Si[i] not in A:
        A[Si[i]] = [i]
    else:
        A[Si[i]].append(i)
possible = func(0, A, Fi)
sumprofit = [sum([Pi[j] for j in i]) for i in possible]
print(max(sumprofit))
