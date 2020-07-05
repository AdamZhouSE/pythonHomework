x=float(input())
n=int(input())
result=1.0
if n<0:
    x=1.0/x
    n=-n
while n>0:
    result=result*x
    n=n-1
print('{:.5f}'.format(result))