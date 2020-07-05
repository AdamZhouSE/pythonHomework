import re
def exam3():
    X = re.split("\[|\]|,", input())
    X.remove(X[0])
    X.remove(X[len(X) - 1])
    y = re.split("\[|\]|,", input())
    y.remove(y[0])
    y.remove(y[len(y) - 1])
    a1=[]
    for i in X:
        a1.append(int(i))
    for j in y:
        a1.append(int(j))
    a1.sort()
    print(a1)
exam3()