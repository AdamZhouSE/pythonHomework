numbers=list(map(int,input().split(",")))
sum=0
length=0
dv=numbers[1]-numbers[0]
i=2
while i<len(numbers):
    length=0
    if numbers[i]-numbers[i-1]==dv:
        while i<len(numbers) and numbers[i]-numbers[i-1]==dv:
            length=length+1
            i=i+1
        if i<len(numbers):
            dv=numbers[i]-numbers[i-1]
            i=i+1
        sum=sum+int(length*(length+1)/2)
    else:
        i=i+1
print(sum)