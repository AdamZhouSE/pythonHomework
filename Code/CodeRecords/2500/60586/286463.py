import re

def exam4():
    X = re.split("\[|\]|,", input())
    X.remove(X[0])
    X.remove(X[len(X) - 1])
    a=[]
    n=[]
    for item in X:
        a.append(int(item))
    for i in range(len(a),0,-1):
        loc=a.index(i)
        n.append(loc+1)
        n.append(i)
        a[:loc+1]=a[:loc+1][::-1]
        a[:len(a)-i]=a[:len(a)-i][::-1]
    print(n)
exam4()