c=int(input())
find=False
for i in range(c):
    for j in range(c):
        if(i**2+j**2==c):
            find=True
            
print(find)