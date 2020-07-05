temp=[int(x) for x in input().split(',')]
k=int(input())
find=False
for i in range(len(temp)):
    sum=0
    for j in range(i,len(temp)):
        sum+=temp[j]
        if(sum%k==0 and j-i>=1):
            find=True
            break
    if(find):
        break
        
print(find)
            