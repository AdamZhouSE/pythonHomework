a=int(input())
while a>=10:
    x=str(a)
    sum=0
    for i in range(0,len(x)):
        sum=sum+int(x[i])
    a=sum
print(a)