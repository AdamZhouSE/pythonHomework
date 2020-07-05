size=int(input())
array=list(map(int,input().split(' ')))
sum=0
for i in range(size):
    sum=sum+array[i]
if(sum%2==1):
    array.sort()
    for i in range(size):
        if(array[i]%2==1):
            sum=sum-array[i]
            break
print(sum)