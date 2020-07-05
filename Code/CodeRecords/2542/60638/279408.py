numbers=list(map(int,input()[1:-1].split(",")))
numbers.sort()
length=0
for i in range(0,len(numbers)-1):
    k=1
    while numbers[i+1]==numbers[i]+1:
        k=k+1
        i=i+1
    length=max(length,k)
print(length)