a = input()
num = a[0:]
if a[0]=='-':
    num = a[1:]
result = list(reversed(num))
b = ""
if a[0]=='-':
    b=b+a[0]
for i in result:
    b+=i
print(b.lstrip("0"))