a=float(input())
b=int(input())
result=1.0
if(b>0):
    for i in range(0,b):
        result=result*a
elif b==0:
    result=1
else:
    for i in range(b,0):
        result=result/a
print(result)