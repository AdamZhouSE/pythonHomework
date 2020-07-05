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
    b = sorted(range(1, N + 1), key=lambda i: -a[i - 1])
    for i in b:
        for f in n:
            if i <= f:
                i = f + 1 - i
        n.extend([i, N])
        N -= 1
    print(n)
exam4()