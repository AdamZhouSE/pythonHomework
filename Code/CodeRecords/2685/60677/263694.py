times=int(input())
for i in range(times):
    n=int(input())
    x=n%9
    y=n//9
    z=""
    for i in range(0,y):
       z=z+"9"
    for i in range(n):
        z=z+"0"
    print(str(x)+z)