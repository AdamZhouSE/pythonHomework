import re

def exam4():
    X = re.split("\[|\]|,", input())
    X.remove(X[0])
    X.remove(X[len(X) - 1])
    a=[]
    n=[]
    for item in X:
        a.append(int(item))
    N = len(a)
    while N:
        idx = a.index(N)
        n.append(idx + 1)
        a = a[:idx + 1][::-1] + a[idx + 1:]
        n.append(N)
        a = a[:N][::-1] + a[N:]
        N -= 1
    print(n)
exam4()