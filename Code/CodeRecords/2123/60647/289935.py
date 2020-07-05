n=int(input())
a=0
for i in range(n):
    if i*i==n:
        a=1
if a==1:
    print('True')
else:
    print('False')