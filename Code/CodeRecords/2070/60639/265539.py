x=float(input())
n=int(input())
result=x
if n>0:
    for i in range(n - 1):
        result = result * x
else:
    for i in range(-n-1):
        result=result*x
    result=1/result
print('{:.5f}'.format(result))