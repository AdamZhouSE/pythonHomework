import re
def exam8():
    X = re.split("\[|\]|,", input())
    X.remove(X[0])
    X.remove(X[len(X) - 1])
    num=[]
    d=[]
    for x in X:
        num.append(int(x))
    low=int(input())
    up=int(input())
    for j in range(1,len(num)):
        for  i in range(0,j):
            s=sum(num[i,j+1])
            if s>=low or s<=up:
                d.append(s)
    print(len(d))
exam8()