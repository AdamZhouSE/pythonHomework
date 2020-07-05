def binaryToint(l):
    tmp=1
    res=0
    for i in range(1,len(l)+1):
        res+=l[-i]*tmp
        tmp*=-2
    return res
def intTobinary(n):
    if n == 0:
        return ([0])
    else:
        digits = []
        while n != 0:
            n, r = divmod(n, -2)
            if r < 0:
                n += 1
                r += 2
            digits.append(r)
        return (digits[::-1])
arr1=list(map(int,input().split(",")))
arr2=list(map(int,input().split(",")))
print(intTobinary(binaryToint(arr1)+binaryToint(arr2)))