n=int(input())
result=10
x=9
for i in range(2,n+1):
    x=x*(11-i)
    result=result+x
print(result)