a = input()
b = input()
c = input()
if a<b:
    if b<c:
        print(a)
        print(b)
        print(c)
    else:
        if a<c:
            print(a)
            print(c)
            print(b)
        else:
            print(c)
            print(a)
            print(b)
elif a>b:
    if b>c:
        print(c)
        print(b)
        print(a)
    else:
        if c<a:
            print(b)
            print(c)
            print(a)
        else:
            print(b)
            print(a)
            print(c)