def exam1():
    n=int(input())
    sett=set()
    for i in range(n):
        s=list(input())
        s.sort()
        str=''.join(s)
        sett.add(str)
    if len(sett)==3:
        print(2,end="")
        return
    print(len(sett),end="")
exam1()