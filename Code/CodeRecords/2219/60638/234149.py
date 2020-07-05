n = int(input())
x=False
for i in range(1,n):
    for j in range(1,i+1):
        if i*i+j*j==n:
            print(True)
            x=True
        elif i*i+j*j>n:
            break
if x==False:
    print(False)