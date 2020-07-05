a=float(input())
b=int(input())
rs=1
if b>0:
    for i in range(b):
        rs*=a
    print('%.5f'%rs)
if b<0:
    for i in range(-b):
        rs/=a
    print('%.5f'%rs)