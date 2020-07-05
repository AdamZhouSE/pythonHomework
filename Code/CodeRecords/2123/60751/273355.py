num=int(input())
i=1
k=False
while(i*i<=num):
    if i**2==num:
        k=True
    i+=1
print(k)
