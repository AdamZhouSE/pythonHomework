nums=list(map(int,input().split(' ')))
sizes=list(map(int,input().split(' ')))
size=nums[0]
t=nums[1]
total=0
maxsize=0
i=0
j=0
while i<size:
    total=total+sizes[i]
    if(total>t):
        total=total-sizes[j]
        j=j+1
        maxsize=max(maxsize,i-j)
    i=i+1
maxsize=max(maxsize,i-j)
print(maxsize)