f=float(input())
n=int(input())
temp=f
i=1
if(n>0):
    while i<n:
        f=temp*f

        i+=1
    print('%.5f' % f)

else:
    n=0-n
    i=1
    while i<n:
        f=temp*f
        i+=1
    f=1/f
    print('%.5f' % f)