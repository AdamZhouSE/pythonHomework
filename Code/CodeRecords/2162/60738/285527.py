a=float(input())
b=int(input())
result=a
if b>0:
    for i in range (b-1):
        result*=a
elif b<0:
    for j in range(-b-1):
        result*=a
    result=1.0/result
else:
    print("1.00000")
print('%.5f'%result)
