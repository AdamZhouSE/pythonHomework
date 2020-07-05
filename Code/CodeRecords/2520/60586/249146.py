def exam1():
    r=int(input())
    c=int(input())
    r0=int(input())
    c0=int(input())
    arr=[]
    x=[]
    for i in range(r):
        for j in range(c):
            arr.append([abs(r0 - i) + abs(c0 - j), [i, j]])
    arr=sorted(arr, key=lambda x: x[0])
    for item in arr:
        x.append(item[1])
    print(x)
exam1()