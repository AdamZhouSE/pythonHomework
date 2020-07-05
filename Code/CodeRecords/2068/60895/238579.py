a=int(input())
b=int(input())
result=0
if a>=0 and b>0:
    while a>=0:
        a=a-b
        result=result+1
    result=result-1
elif a>=0 and b<0:
    while a>=0:
        a=a+b
        result=result-1
    result=result+1
elif a<=0 and b>0:
    while a<=0:
        a=a+b
        result=result-1
    result=result+1
else:
    while a<=0:
        a=a-b
        result=result+1
    result=result-1
print(result)