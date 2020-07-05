def exam1():
    n=int(input())
    arr=[]
    for i in range(n):
        s=input()
        s=sorted(s)
        arr.append(s)
    a=sorted(arr)
    ind=1
    for i in range(1,n):
        if a[i]!=a[i-1]:
            ind+=1
    print(ind)
exam1()