x=int(input())
y=int(input())
num=0
while x<y:
    num+=1
    if y%2==0:
        y//=2
    else:
        y+=1
print(num+x-y)