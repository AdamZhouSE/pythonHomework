num = [int(n) for n in (input()[1:-1]).split(",")]
for i in range(0,len(num)):
    for j in range(i+1,len(num)):
        if(num[i]>=num[j]):
            temp=num[i]
            num[i]=num[j]
            num[j]=temp
print(num)         