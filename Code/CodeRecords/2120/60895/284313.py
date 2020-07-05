n=int(input())
result=1
if n==2:
    result=1
elif n==3:
    result=2
elif n==4:
    result=4
else:
    while n>4:
        result=result*3
        n=n-3
    result=result*n
print(result)