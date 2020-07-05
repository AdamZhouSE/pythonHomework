import re
def exam6():
    X = re.split("\[|\]|,", input())
    X.remove(X[0])
    X.remove(X[len(X) - 1])
    a=[]
    n=[]
    for i in X:
        a.append(int(i))
    for i in range(len(a)):
        num=0
        for j in range(i+1,len(a)):
            if a[j]<a[i]:
                num=num+1
        n.append(num)
    print(n)
exam6()