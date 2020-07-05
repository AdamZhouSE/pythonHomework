n=int(input())
count=10
if n==0:
    count=0
if n==1:
    count=10
if n>=2:
    count=10
    temp=81
    for i in range(2,n):
        temp=temp*(10-i)
    count=count+temp
print(count)