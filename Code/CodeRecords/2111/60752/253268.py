num=int(input())
count=0
b=0
while count!=num:
    b+=1
    a=b
    while a%2==0:
        a=a/2
    while a%3==0:
        a=a/3
    while a%5==0:
        a=a/5
    if a==1:count+=1
print(b)