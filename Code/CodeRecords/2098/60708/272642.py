A=65
result=''
n= int(input())
while(n!=0):
    if n%26!=0:
        result=chr(A+int(n%26)-1)+result
    else:
        result=chr(A+26-1)
    n=int(n/26)
print(result)