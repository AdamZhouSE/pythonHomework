import  math
c=int(input())
maxSize=int(math.floor(math.sqrt(c)))
a=False

for i in range(0,c+1):
    for j in range(i,c+1):
        if i*i+j*j==c:
            a=True

if a:
    print(True)
else:
    print(False)

