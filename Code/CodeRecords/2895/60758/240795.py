a=input()
a=eval(a)
result=-1
for i in range(a[0],a[-1]+1):
    result=result&i
print(result)