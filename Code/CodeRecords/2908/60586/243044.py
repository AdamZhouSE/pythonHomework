def exam1():
    n=int(input())
    arr=[]
    for i in range(n):
        s=list(input())
        s.sort()
        string=''.join(s)
        arr.append(string)
    print(len(set(arr)),end="")
exam1()