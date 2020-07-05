stones=list(map(int,input().split(',')))
i,j=0,len(stones)-1
Alex,Lee=0,0
for k in range(len(stones)):
    stone=0
    if stones[i]>=stones[j]:
        stone=stones[i]
        i+=1
    else:
        stone=stones[j]
        j-=1
    if k%2==0:
        Alex+=stone
    else:
        Lee+=stone
print(Alex>Lee)