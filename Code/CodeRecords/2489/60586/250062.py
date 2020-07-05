import re
def exam8():
    X = re.split("\[|\]|,", input())
    X.remove(X[0])
    X.remove(X[len(X) - 1])
    num=[]
    for x in X:
        num.append(int(x))
    num.sort()
    low=int(input())
    up=int(input())
    n=0
    for item in num:
        if item>=low&item<=up:
            n=n+1
    print(n)
exam8()