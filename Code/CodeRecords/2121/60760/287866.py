n=int(input())
count=10
if n==0:
    count=0
if count==1:
    count=10
if count>1:
    temp=9
    for i in range(2,n+1):
        temp=temp*(11-i)
    count=count+temp
print(count)
