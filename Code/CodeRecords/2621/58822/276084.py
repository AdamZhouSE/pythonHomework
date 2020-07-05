n=input()
b=list(eval(n))
max=0
sum=0
for i in range(len(b)):
    sum=0
    if(b[i]>=0):
        sum=b[i]
        for k in range(i+1,len(b)):
            sum=sum+b[k]
            if(sum>max):
                max=sum
        if(sum>max):
            max=sum
print(max)