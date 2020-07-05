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
    num=0
    for item in num:
        if item>=low&item<=up:
            num=num+1
    print(num)
exam8()