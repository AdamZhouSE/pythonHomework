numbers=list(map(int,input().split(",")))
length=1
res=[1]
for i in range(1,len(numbers)):
    lengthN=1
    for j in range(0,i):
        if numbers[j]<=numbers[i]:
            lengthN=max(lengthN,res[j]+1)
    res.append(lengthN)
print(res[-1])