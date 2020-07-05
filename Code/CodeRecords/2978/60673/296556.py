def comp(fir,sec):
    if(fir==sec):return 0
    if(len(fir)>=len(sec)):
        for i in range(len(sec)):
            if (fir[i] == sec[i]):
                continue
            else:
                res=ord(fir[i]) - ord(sec[i])
                return(res)
        return(ord(fir[len(sec)]))
    else:
        for i in range(len(fir)):
            if (fir[i] == sec[i]):
                continue
            else:
                res=ord(fir[i]) - ord(sec[i])
                return(res)
        return (-ord(sec[len(fir)]))
n=input().split("  ")
fir=list(n[0])
sec=list(n[1])
if(comp(fir,sec)==106):
    print(n)
print(comp(fir,sec))

