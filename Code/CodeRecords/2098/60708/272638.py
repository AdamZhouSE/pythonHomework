A=65
result=''
n= int(input())
while(n!=0):
    result=chr(A+int(n%27)-1)+result
    n=int(n/26)
print(result)