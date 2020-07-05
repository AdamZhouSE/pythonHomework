def move(numbers,i):
    sum=0
    for num in numbers:
        sum=sum+abs(num-i)
    return sum
numbers=list(map(int,input().split(",")))
sum=0
for num in numbers:
    sum=sum+num
minN=10000
j=0
for i in range(0,max(numbers)+1):
    k=move(numbers, i)
    if k<minN:
        j=i
        minN=k
print(move(numbers,j))
