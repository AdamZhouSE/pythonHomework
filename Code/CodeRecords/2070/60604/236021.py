a=float(input())
aa=a
b=int(input())
if b>0:
    while(b>1):
        aa=aa*a

        b-=1
else:
    while(b<-1):
        aa=aa*a

        b+=1
    aa=1/aa
print('%.5f' % aa)