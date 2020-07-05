a=float(input())
b=int(input())
result=1.00000
if(b>0):
    for i in range(0,b):
        result=result*a
elif b==0:
    result=1
else:
    for i in range(b,0):
        result=result/a
print("%0.5f"%result)