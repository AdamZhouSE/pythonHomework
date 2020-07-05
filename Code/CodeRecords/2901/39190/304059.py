def func12(num):
    tmp=num%2
    num=(num-tmp)/2
    while num>=1:
        if num%2==1:
            tmp1=1
        else:
            tmp1=0
        if tmp==tmp1:
            return False
        else:
            tmp=tmp1
            num=(num-tmp)/2
    return True
ip=int(input())
op=func12(ip)
print(op)