a=float(input())
b=int(input())
result=1
if(b>0):
    for i in range(0,b):
        result=result*a
elif b==0:
    result=1
else:
    result=result/a
print(result)