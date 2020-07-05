n=int(input())
a=int(input())
b=int(input())
c=int(input())
i=0
num=1
answer=0
if b>2*10**8:
    b=1
if c>2*10**8:
    c=1
while i<n:
    if num%a==0 or num%b==0 or num%c==0:
        i=i+1
        answer=num
    num+=1
print(answer)