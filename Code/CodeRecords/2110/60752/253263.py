a=int(input())
while a%2==0:
    a=a/2
while a%3==0:
    a=a/3
while a%5==0:
    a=a/5
print(a==1)