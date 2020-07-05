def getkp(lst, k):
    fac = 1
    if(k == 1):
        return ''.join(lst)
    for i in range(1, len(lst)):
        fac *= i
    fir = lst[k // fac]
    lst.remove(fir)
    return fir + getkp(lst, k % fac)

    
n = int(input())
k = int(input())
lst = [str(x + 1) for x in range(n)]
print(getkp(lst, k))
