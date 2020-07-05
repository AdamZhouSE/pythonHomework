def reorderedPowerOf2(N):
    sn=str(N)
    sn = "".join((lambda x:(x.sort(),x)[1])(list(sn)))
    max=int(sn[::-1])
    pow=1
    while pow<=max:
        spow=str(pow)
        spow="".join((lambda x:(x.sort(),x)[1])(list(spow)))
        if spow==sn:
            return True
        pow*=2
    return False

n=int(input())
print(reorderedPowerOf2(n))