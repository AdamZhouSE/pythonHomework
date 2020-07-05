import re
def exam7():
    X = re.split("\[|\]|,", input())
    X.remove(X[0])
    X.remove(X[len(X) - 1])
    arr=[]
    for i in X:
        arr.append(int(i))
    if len(arr)==2:
        print(arr.sort())
    else:
        arr.sort()
        temp=arr[1]
        arr[1]=arr[2]
        arr[2]=temp
        print(arr)
exam7()
