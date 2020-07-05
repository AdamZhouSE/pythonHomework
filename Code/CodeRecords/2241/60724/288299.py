N=int(input())
num=0
for i in range(1,N+1):
    for j in range(i,N+1):
        if (i+j)*(j-i+1)//2==N:
            num+=1
print(num)