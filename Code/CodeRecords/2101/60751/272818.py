def oper(num):
    result=0
    for i in str(num):
        result+=int(i)**2
    return result
op=int(input())
a=False
for i in range(1000):
    op=oper(op)
    if op==1:
        a=True
        break
print(a)
