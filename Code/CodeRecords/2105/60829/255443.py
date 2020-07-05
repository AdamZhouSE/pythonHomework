def k(x):
    if x<0:
        x=-1*x
    return x

a=str(input())
x=k(int(int(a[0])-int(a[4])))*k(int(int(a[2])-int(a[6])))
y=k(int(int(a[8])-int(a[12])))*k(int(int(a[10])-int(a[14])))
print(x+y)