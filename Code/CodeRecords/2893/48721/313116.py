a=eval(input())
a.sort()

if a[0]!=a[1]:
    print(a[0])
else:
    m=len(a)
    print(a[m-1])