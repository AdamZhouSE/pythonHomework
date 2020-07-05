def solve():
    num=int(input())
    res1=sum(map(int,list(str(num))))

    factors=[]
    while num>1:
        for fac in range(2,num+1):
            if num%fac==0:
                factors.append(fac)
                num=int(num/fac)
                break
    if len(factors)==1:
        print(0)
        return 
    res2=sum(map(int,list(''.join(map(str,factors)))))
    if res1==res2:
        print(1)
    else:
        print(0)

if  __name__ == '__main__' :
    totle=int(input())
    for i in range(totle):
        solve()