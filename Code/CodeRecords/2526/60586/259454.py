import re
def exam3():
    X = re.split("\W", input())
    X.remove(X[0])
    X.remove(X[len(X) - 1])
    y = re.split("\W", input())
    y.remove(y[0])
    y.remove(y[len(y) - 1])
    a1=[]
    for i in X:
        if i!='null':
            a1.append(int(i))
    for j in y:
        if j!='null':
            a1.append(int(j))
    a1.sort()
    print(a1)
exam3()