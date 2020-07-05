n=int(input())
result=""
if n==1 or n<0:
    result=False
count=1
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        count+=i+n/i
if result==False:
    result=result
elif count==n:
    result=True
else:
    result=False
print(result)