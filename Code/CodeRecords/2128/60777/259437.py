temp=[int(x) for x in input().split(',')]
maxf=0
for i in range(len(temp)):
    maxf+=i*temp[i]
for i in range(len(temp)):
    sum=0
    for j in range(len(temp)):
        sum+=j*temp[(i+j)%len(temp)]
    if(maxf<sum):
        maxf=sum
        
print(maxf)