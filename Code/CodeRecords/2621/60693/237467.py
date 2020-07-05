numbers=input().split(',')
sum=int(numbers[0])
maxsum=sum
for i in range(1,len(numbers)):
    if sum>0:
        sum+=int(numbers[i])
        if sum>maxsum:
            maxsum=sum
    else:
        sum=int(numbers[i])
        if sum>maxsum:
            maxsum=sum
print(maxsum)