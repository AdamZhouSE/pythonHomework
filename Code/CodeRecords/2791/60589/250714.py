n=int(input())
nums=input().split(' ')
nums=list(map(int,nums))
i=0
stairs=[]
while i<n:
    count=1
    while i+count<n and nums[i+count]!=1:
        count=count+1
    i=i+count
    stairs.append(count)
print(len(stairs))
stairs=list(map(str,stairs))
print(' '.join(stairs))