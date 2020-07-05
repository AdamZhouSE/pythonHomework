import re

def exam1():
    x=input()
    X=re.split("\[|\]|,",x)
    X.remove(X[0])
    X.remove(X[len(X)-1])
    arr=[]
    for item in X :
        arr.append(int(item))
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            flit=i
    for i in range(flit,len(arr)):
        if arr[i-1]<=arr[i]:
            break;
    print(flit)
exam1()