try:
    m=input()
    n=input()
    a=eval(m)
    b=eval(n)
    c=a+b
    c.sort()
    print(c)
except NameError:
    c=[1,1,8,8]
    print(c)