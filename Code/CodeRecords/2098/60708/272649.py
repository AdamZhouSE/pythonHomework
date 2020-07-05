
result=''
n= int(input())
if n==1:
    result='A'
while(n!=1):
    if n%26!=0:
        result=chr(65+int(n%26)-1)+result
    else:
        result=chr(65+26-1)+result
    n=int(n/26)
print(result)