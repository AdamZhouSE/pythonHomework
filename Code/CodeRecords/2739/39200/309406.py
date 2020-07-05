def func(start, k, n):
    if n < start:
        return [[]]
    elif n == start and k == 1:
        return [[start]]
    elif n == start and k != 1:
        return [[]]
    elif start == 9:
        return [[]]
    else:
        returnval = []
        for x in func(start + 1, k, n):
            if x != []:
                a = []
                a.extend(x)
                returnval.append(a)
        for x in func(start + 1, k - 1, n - start):
            if x != []:
                a = [start]
                a.extend(x)
                returnval.append(a)
        return returnval


k, n = [int(x) for x in input().split(",")]
print(func(1, k, n)[::-1])
