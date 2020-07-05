def func(start, A, Fi):
    if start > max(A.keys()):
        return [[]]
    while start not in A:
        start += 1
    if start == max(A.keys()):
        return [[A[start][0]]]
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
        


t = int(input())
for x in range(t):
    n = int(input())
    Si = [int(i) for i in input().split()]
    Fi = [int(i) for i in input().split()]
    A = {}
    for i in range(n):
        if Si[i] not in A:
            A[Si[i]] = [i]
        else:
            A[Si[i]].append(i)
    possible = func(0, A, Fi)
    length = [len(i) for i in possible]
    indexoflongestpossible = len(length) - 1 - length[::-1].index(max(length))
    for i in range(max(length)):
        print(possible[indexoflongestpossible][i] + 1, end=" ")
    print()
