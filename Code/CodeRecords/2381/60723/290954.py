array1=input().split(',')
array1=array1[::-1]
array2=input().split(',')
array2=array2[::-1]
ans=0
for i in range(len(array1)):
    ans=ans+(-2)**i
for j in range(len(array2)):
    ans=ans+(-2)**j
print(ans)