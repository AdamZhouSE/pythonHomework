
result=''
n= int(input())
while(n!=0):
    if n%26!=0:
        result=chr(65+int(n%26)-1)+result
    else:
        result=chr(65+26-1)+result
    n=int(n/26)
    if(n==1):
        break
print(result)