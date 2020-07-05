a=eval(input())
for i in range(a):
    num = eval(input())
    t0=1
    t1=1
    j=1
    while j<num:
        j+=1
        temp=t0
        t0=t1
        t1=t0+temp
    print(t1+t0)

