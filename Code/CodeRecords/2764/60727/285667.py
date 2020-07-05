def so(n):
    a=n//2+n//3+n//4
    if n>=a:
        return n
    else:
        return so(n//2)+so(n//3)+so(n//4)
for i in range(0,eval(input())):
    a = eval(input())
    print(so(a))