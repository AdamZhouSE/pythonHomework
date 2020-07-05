x=int(input())
y=int(input())
z=int(input())
if x>y:
    min=y
else:
    min=x
while min>0:
    if x%min==0 and y%min==0:
        gcd=min
        break
    else:
        min=min-1
if z%min==0:
    result=True
else:
    result=False
print(result)