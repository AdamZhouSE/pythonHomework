def pow(x,d):
    z=1
    for i in range(0,d):
        z=z*x
    return z
a=int(input())
b=int(input())
c=int(input())
d=int(c//b)
x=2
while pow(x,d)<a:
    x=x+1
print(x-1)