numbers=list(map(int,input()[1:-1].split(",")))
count=0
for i in range(0,len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]>numbers[j]*2:
            count=count+1
print(count)