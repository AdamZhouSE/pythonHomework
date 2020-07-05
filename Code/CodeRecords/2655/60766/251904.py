n=int(input())
for i in range(n):
    a=int(input())
    i=0
    t=0
    while t<a:
        t=pow(2, i)
        i=i+1
    print(t)