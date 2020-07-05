import functools

def n_to_ten(n):
    def f(l):
        if l:
            return functools.reduce(lambda x, y: x * n + y, map(int, l))
        return 'x'
    return f

def finding(s2,s3):
    f2 = n_to_ten(2)
    f3 = n_to_ten(3)
    for i in range(1) if s2[0] == '0' else range(len(s2)):
        for j in range(1) if s3[0] == '0' else range(len(s3)):
            ns3 = s3[:]
            ns2 = s2[:]
            for k in filter(lambda x: x != s2[i], [0, 1] if i != 0 else [1]):
                for r in filter(lambda x: x != s3[j], [0, 1, 2] if j != 0 else [1, 2]):
                    ns2[i] = k
                    ns3[j] = r
                    if f2(ns2) == f3(ns3):
                        return f2(ns2)
    return -1


s2=list(input().split()[0])
s3=list(input().split()[0])
print(finding(s2,s3),end='')