def reverse(l,n):
    res = []
    for i in range(n+1):
        res.append(l[n-i])
    for i in range(len(l)-n-1):
        res.append(l[n+i+1])
    return res


def solve(l,res):
    if len(l)==1:
        return res
    else:
        n = l.index(max(l))
        if n != len(l)-1:
            if n != 0:
                l = reverse(l, n)
                res.append(n+1)
                res = solve(l,res)
            else:
                l = reverse(l,len(l)-1)
                res.append(len(l))
                res = solve(l[:-1],res)
        else:
            res = solve(l[:-1],res)
    return res


string = input()
l = string[1:-1].split(",")
for i in range(len(l)):
    l[i] = int(l[i])
print(solve(l,[]))