# https://coordinate.wang/index.php/archives/2634/
# 二分法查找
def solve():
    def gcd(a,b):
        while b:
            a,b=b,a%b
        return a
    def lcm(a,b):
        return a*b//gcd(a,b)
    def lcm3(a,b,c):
        return lcm(a,lcm(b,c))
    def count3(k,a,b,c):
        return k//a+k//b+k//c-k//lcm(a,b)-k//lcm(b,c)-k//lcm(a,c)+k//lcm3(a,b,c)

    n,a,b,c=[int(input()) for i in range(4)]
    left,right=1,2*10**9
    while left<right:
        mid=(left+right)>>1
        if count3(mid,a,b,c)<n:
            left=mid+1
        else:
            right=mid
    print(left)
    
if  __name__ == '__main__' :
    solve()
    
            