def selfDividingNum(left,right):
    def is_self_dividing(n):
        for i in str(n):
            if i=='0' or n%int(i)>0:
                return False
        return True
    ret=[]
    for i in range(left,right+1):
        if is_self_dividing(i):
            ret.append(i)
    return ret

left=int(input())
right=int(input())
print(selfDividingNum(left,right))

