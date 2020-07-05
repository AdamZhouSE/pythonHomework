n=int(input())
a=int(input())
b=int(input())
c=int(input())
low=min(a,b,c)
high=2*pow(10,10)
def lcm(a,b):
    s,m=a,b
    while b>0:
        temp=a
        a=b
        b=temp%b
    return s*m//a
def ugly(low,high,a,b,c,n):
    while low<high:
        mid = low+(high-low)//2
        temp= mid // a + mid // b + mid // c - mid // lcm(a, b) - mid // lcm(a, c) - mid // lcm(b, c) + mid // lcm(a * b, c)
        if temp==n:
            return mid
        elif temp<n:
            low=mid+1
        else:
            high=mid
    return 0
res=ugly(low,high,a,b,c,n)
left_a=res%a
left_b=res%b
left_c=res%c
print(res-min(left_a,left_b,left_c))