n=int(input())
com=1
for i in range(1,n):
    a = i * i
    for j in range(1,n):
        b=j*j
        c=a+b
        if c==n:
           com=0
           break
if com==1:
   print('False')
else:
   print('True')