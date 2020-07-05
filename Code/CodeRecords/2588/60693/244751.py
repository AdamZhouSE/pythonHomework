def get_prime_factors(n):
    res=[]
    i=2
    while i<=n:
        if n%i==0:
            n=n//i
            res.append(i)
            i-=1
        i+=1
    return res

cases=int(input())
for i in range(cases):
    num=int(input())
    factors=get_prime_factors(num)
    if len(factors)==1:print('0')
    else:
        arr_num=list(str(num))
        arr_fac=list(''.join(list(map(str,factors))))
        sum_num=sum(map(int,arr_num))
        sum_fac=sum(map(int,arr_fac))
        if sum_num==sum_fac:print('1')
        else:print('0')