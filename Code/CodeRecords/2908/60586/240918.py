def exam1():
    n=int(input())
    sett=set()
    for i in range(n):
        s=list(input())
        s.sort()
        str=''.join(s)
        sett.add(str)
    print(len(sett))
exam1()