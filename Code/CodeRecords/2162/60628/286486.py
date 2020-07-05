def pow(x, n):
    if n < 0 :
        return pow(1/x, -n)
    if n == 0 :
        return 1
    if n == 2 :
        return x*x
    return pow(pow(x, n/2),2) if not n%2 else x* pow(pow(x, n//2),2)

x = float(input())
n = int(input())
print(("%.5f" % pow(x, n)))