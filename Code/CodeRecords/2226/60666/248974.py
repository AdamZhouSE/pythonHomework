left=int(input())
right=int(input())
result=[]
for i in range(left,right+1):
    for j in str(i):
        if j=='0' or i%int(j)!=0:
            break
    else:
        result.append(i)
print(result)