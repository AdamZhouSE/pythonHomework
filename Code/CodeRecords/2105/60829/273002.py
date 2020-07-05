def k(x):
    if x<0:
        x=-1*x
    return x
def max(x,y):
    if x>=y:
        return x
    else:
        return y
a=str(input()).split(",")
x=k(int(int(a[0])-int(a[2])))*k(int(int(a[1])-int(a[3])))
y=k(int(int(a[4])-int(a[6])))*k(int(int(a[5])-int(a[7])))
z=k(max(a[0],a[4])-max(a[2],a[6]))*k(max(a[1],a[5])-max(a[3],a[7]))
print(x+y-z)