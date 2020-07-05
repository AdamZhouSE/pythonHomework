def add(numbers,j):
    for i in range(0,len(numbers)):
        if i!=j:
            numbers[i]=numbers[i]+1
def check(numbers):
    res=True
    for i in range(1,len(numbers)):
        if numbers[i]!=numbers[i-1]:
            res=False
            break
    return res
def findMax(numbers,maxN):
    for i in range(0,len(numbers)):
        if numbers[i]==maxN:
            return i
numbers=list(map(int,input().split(",")))
sum=0
for num in numbers:
    sum=sum+num
count=1
while True:
    maxN = max(numbers)
    i=findMax(numbers,maxN)
    add(numbers,i)
    if check(numbers):
        break
    count=count+1
print(count)