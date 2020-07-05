a=int(input())
temp=input()
b=""
for item in temp:
    if(item!=','):
        b=b+item
b=int(b)
result=1
for i in range(b,0,-1):
    result=result*a
print(result%1337)