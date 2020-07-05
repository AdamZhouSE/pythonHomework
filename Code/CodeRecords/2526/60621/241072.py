try:
    a=[int(x) for x in input().replace("\'null\'","").lstrip("[").rstrip("]").split(",")]
    b=eval(input())
except BaseException:
    print(a)
    print(b)
a[len(a):len(a)]=b
a.sort()
print(a)