a=int(input())
b=int(input())
c=int(input())
d=int(c//b)
count=0
s=d
while s<a:
    s=s*d
    count=count+1
print(count)