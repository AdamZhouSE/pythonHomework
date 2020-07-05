a=eval(input())
b=input().split(',')
c=''
for i in b:
    c=c+i
c=eval(c)
print((a**c)%1337)