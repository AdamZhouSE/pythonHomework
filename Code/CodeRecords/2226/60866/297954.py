def selfDividingNumbers(left,right):
    l=[]
    for i in range(left,right+1):
        a=str(i)
        if '0' in a:
            continue
        else:
            tem=[]
            for j in a:
                tem.append(i%int(j)==0)
            if all(tem):
                l.append(i)
    return l
left=int(input())
right=int(input())
print(selfDividingNumbers(left,right))