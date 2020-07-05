#最大公因数
def GCD(a,b):
    while b>0:
        temp=a%b
        a=b
        b=temp
    return a#是a啊不是b

#最小公倍数
def MCM(a,b):
    return a*b/GCD(a,b)

#二分搜索
def binSearch(low,high,n,a,b,c):
    if low>=high:
        return low
    else:
        middle=(low+high)>>1#相当于模200.
        #独立的丑数个数为，当前数分别除以a、b、c,相加求和，减去当前数除以a、b、c两两间最小公倍数的和，再加上当前数除以 a、b、c三者的最小公倍数 就等于[low,当前数]之间的丑数因子！的数量
        temp=int(middle//a+middle//b+middle//c-middle//MCM(a,b)-middle//MCM(b,c)-middle//MCM(a,c)+middle//MCM(MCM(a,b),c))#temp是low边界到当前位置之间丑数因子的个数
        if temp==n:
            return middle
        elif temp<n:
            return binSearch(middle+1,high,n,a,b,c)#middle+1!!
        else:
            return binSearch(low,middle-1,n,a,b,c)#middle-1!!!

def nthUglyNum(n:int,a:int,b:int,c:int):
    low=min(a,b,c)
    high=low*n
    roughRange=binSearch(low,high,n,a,b,c)
    res=roughRange-min(roughRange%a,roughRange%b,roughRange%c)
    return res
    #比如第n个丑数是X，那么[X,X + min(a,b,c))这个半开区间内的所有数都同时包含n个丑数因子，
    # 我们通过二分法得到的答案也随机分布于这个区间中。而实际上我们只需要得到该区间的左端即可。
    # 处理方法很简单：假设我们得到的临时答案是K(K∈[X,X + min(a,b,c))),那么K - min(K%a,K%b,K%c) = X.
    # 也就是只需要把临时答案减去其与a、b、c三者中取余的最小值即可！


if __name__=="__main__":
    n=int(input())
    a=int(input())
    b=int(input())
    c=int(input())
    ans=nthUglyNum(n,a,b,c)
    print(ans)