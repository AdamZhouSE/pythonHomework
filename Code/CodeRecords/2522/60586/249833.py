import re
def exam2():
    X = re.split("\[|\]|,", input())
    X.remove(X[0])
    X.remove(X[len(X) - 1])
    y = re.split("\[|\]|,", input())
    y.remove(y[0])
    y.remove(y[len(y) - 1])
    a1=[]
    a2=[]
    arr=[]
    for i in X:
        a1.append(int(i))
    for j in y:
        a2.append(int(j))
    for i in a2:
        for j in a1:
            if j==i:
                arr.append(j)
    for i in a2:
        for j in a1:
            if j == i:
                arr.remove(j)
    a1.sort()
    for i in a1:
        arr.append(i)
    print(arr)
exam2()