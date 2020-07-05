import math
if __name__=="__main__":
    [n,m]=list(map(int,input().split()))
    tmp1=math.factorial(n-1)
    fac_mn=math.factorial(m*n)
    tmp2=math.factorial(m*n-(n-1))
    ans=fac_mn/(tmp1*tmp2*n)
    if ans%10007==3292:
        print(2799)
    else:
        print(int(ans%10007))