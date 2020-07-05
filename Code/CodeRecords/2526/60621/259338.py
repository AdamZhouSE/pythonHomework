try:
    a=input()
    b=input()
    a=eval(a)
    b=eval(b)
except BaseException:
    print(a)
    print(b)
c=a+b
c.sort()
print(c)