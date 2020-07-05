import re

def exam4():
    X = re.split("\[|\]|,", input())
    X.remove(X[0])
    X.remove(X[len(X) - 1])
    a=[]
    n=[]
    for item in X:
        a.append(int(item))
    l=len(a)
    for i in range(l,0):
        loc=a.index(i)
        n.append(loc+1)
        n.append(i)
        a=(a[0:loc+1]).reverse()+a[loc+1:]
        a=(a[0:l]).reverse()+a[l:]
    print(n)
exam4()