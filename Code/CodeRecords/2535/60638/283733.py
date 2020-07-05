def findMin(numbers):
    minN=10000
    j=0
    for i in range(0,len(numbers)):
        if numbers[i]<=minN:
            j=i
            minN=numbers[i]
    return j
def findMax(numbers,x):
    maxN=0
    j=-1
    for i in range(0,len(numbers)):
        if numbers[i]<x and numbers[i]>=maxN:
            j=i
            maxN=numbers[i]
    return j
def Find(numbers,count):
    if len(numbers)==0:
        return count
    if len(numbers)==1:
        return count+1
    minItr=findMin(numbers)
    maxN=max(numbers[0:minItr+1])
    maxItr=findMax(numbers[minItr+1:],maxN)+minItr
    if maxItr==-1+minItr:
        return Find(numbers[minItr+1:],count+1)
    else:
        return Find(numbers[maxItr+1:],count+1)


numbers=list(map(int,input()[1:-1].split(",")))
count=0
count=Find(numbers,count)
print(count)