import re
def exam3():
    x=input()
    X=re.split("\[|\]|,",x)
    X.remove(X[0])
    X.remove(X[len(X)-1])
    arr=[]
    for item in X :
        arr.append(int(item))
    n=int(input())
    if(arr.count(n)==0):
        print(-1)
        return 
    else :
        print(arr.index(n))
exam3()