
result=''
n= int(input())
while(n!=0):
    a=n%26
    if a==0:
        a=26
    result = chr(65 + a - 1) + result
    if n!=26:
        n=int(n/26)
    else:
        break
    
print(result)