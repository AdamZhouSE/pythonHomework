A=65
result=''
n= int(input())
while(n!=0):
    result=result+chr(A+int(n%26)-1)
    n=int(n/26)
print(result)