try:
    c=input()
    a=[int(x) for x in c.replace("\'null\'","").lstrip("[").rstrip("]").split(",")]
    b=eval(input())
except BaseException:
    print(c)
    print(b)
a[len(a):len(a)]=b
a.sort()
print(a)