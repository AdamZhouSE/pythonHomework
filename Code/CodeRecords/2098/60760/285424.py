x=int(input())
res=''
while x>26:
    a=int(x/26)
    x=x%26
    res=res+chr(a+64)
print(res+chr(x+64))