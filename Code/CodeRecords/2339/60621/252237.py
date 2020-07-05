a=eval(input())
for i in range(a):
    b=eval(input())
    c=[int(x) for x in input().split()]
    co=0
    for j in range(b):
        k=j+1
        while k<b:
            if(c[j]>c[k]):
                co+=1
            k+=1
    print(co)