num1=int(input())
num2=int(input())
q=0
if num1<0 and num2>0:
    while num1+num2<=0:
        num1=num1+num2
        q=q+1
    q=-q
elif num1>0 and num2<0:
    while num1+num2>=0:
        num1 = num1 + num2
        q = q + 1
    q = -q
elif num1>0:
    while num1-num2>=0:
        num1=num1-num2
        q=q+1
elif num1<0:
    while num1-num2<=0:
        num1 = num1 - num2
        q = q + 1
print(q)
     