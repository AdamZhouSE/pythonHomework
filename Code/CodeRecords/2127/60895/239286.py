a=input()
b=str(input())
s=','.join(b)
e=int(s)
temp=1
while e>0:
    a=temp*a
    e=e-1
result=a%1337
print(result)