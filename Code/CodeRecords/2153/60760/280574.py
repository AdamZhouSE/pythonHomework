a=input()
if a[0]=='-':
    print(a[0]+a[1:][::-1])
else:
    print(a[::-1])