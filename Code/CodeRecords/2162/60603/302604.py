def x_de_n_cimi(x,n):
    result=1
    for i in range(abs(n)):
        result=result*x
    return result

result=1
x=float(input())
n=int(input())
if n==0:
    print(1)
elif n>0:
    print('%.5f'%x_de_n_cimi(x,n))
else:
    print('%.5f'%float(1/x_de_n_cimi(x,n)))