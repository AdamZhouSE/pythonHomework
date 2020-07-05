x=float(input())
n=int(input())
result=x
for i in range(n-1):
    result=result*x
print('{:.5f}'.format(result))