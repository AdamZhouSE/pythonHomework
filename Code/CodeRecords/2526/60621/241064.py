try:
    a=eval(input())
    b=eval(input())
except BaseException:
    print(a)
    print(b)
a[len(a):len(a)]=b
a.sort()
print(a)