n=int(input())
base=9
digits=1
while n-base*digits>0:
    n=n-base*digits
    base=base*10
    digits=digits+1
index=n%digits
if index==0:
    index=digits
num=(n+digits-1)//digits+base//10

while(index<digits):
    num=num//10
    index=index+1
print(num%10)

