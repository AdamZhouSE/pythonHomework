numbers=list(map(int,input()[1:-1].split(",")))
length=1
maxLen=1
for i in range(0,len(numbers)):
    length=1
    while i<len(numbers)-1 and numbers[i]<numbers[i+1]:
        length=length+1
        i=i+1
    maxLen=max(maxLen,length)
print(maxLen)