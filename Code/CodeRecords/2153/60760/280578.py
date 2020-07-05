a=str(int(input()))
if a[0]=='-':
    print(int(a[0]+a[1:][::-1]))
else:
    print(int(a[::-1]))