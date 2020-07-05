a=int(input())
b=str(input())
s=''
for item in b:
    if item>='0' and item<='9':
        s=s+item
e=int(s)
temp=1
while e>0:
    a=temp*a
    e=e-1
result=a%1337
print(result)