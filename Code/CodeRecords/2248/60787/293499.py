n=int(input())
a=int(input())
b=int(input())
if a<b:
    temp=a
else:
    temp=b
count=0
while count<n:
    if temp%a==0 or temp%b==0:
        count+=1
    temp+=1
re=(temp-1)%1000000007
print(re)