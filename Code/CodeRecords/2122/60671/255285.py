x=int(input())
y=int(input())
z=int(input())
can=False
for i in range(-999,999):
    if(can):
        break
    for j in range(-999,999):
        if(i*x+j*y==z):
            can=True
            break
print(can)