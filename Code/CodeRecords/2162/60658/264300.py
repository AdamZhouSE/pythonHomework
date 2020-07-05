def fast_pow(x,n):
    if n==0:
        return 1
    half = fast_pow(x,n//2)
    if n%2==0:
        return half*half
    else:
        return half*half*x
x = float(input())
y = int(input())
if y<0:
    x=1/x
    y=-y
print("{:.5f}".format(fast_pow(x,y)))