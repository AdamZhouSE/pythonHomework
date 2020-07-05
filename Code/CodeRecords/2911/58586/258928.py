[n,m]=list(map(int,input().split(" ")))
arr=list(map(int,input().split(" ")))
sum=0
temp=0
used=[]
mix=100000007
friends=[]
for i in range(m):
    friends.append(list(map(int,input().split(" "))))
for i in range(m):
    if friends[i][0] not in used and friends[i][1] not in used:
        used.append(friends[i][0])
        used.append(friends[i][1])
        mix=min(arr[friends[i][0]-1],arr[friends[i][1]-1])
        for j in range(m):
            if friends[j][0] in used and friends[j][1] not in used:
                mix=min(arr[friends[j][1]-1],mix)
                used.append(friends[j][1])
            elif friends[j][1] in used and friends[j][0] not in used:
                used.append(friends[j][0])
                mix=min(arr[friends[j][0]-1],mix)
        sum+=mix
for i in range(n):
    if i+1 not in used:
        sum+=arr[i]
print(sum)
