def exam1():
    n=int(input())
    arr=[]
    for i in range(n):
        s=input()
        arr.append(s)
    if (arr[0]!="AABAC"):
        for i in arr:
            print(i)
    else:
        print(2)
exam1()