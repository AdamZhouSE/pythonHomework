numbers=list(map(int,input()[1:-1].split(",")))
numbers.sort()
maxN=0
for i in range(0,len(numbers)-1):
    x=numbers[i+1]-numbers[i]
    if maxN<x:
        maxN=x
print(maxN)