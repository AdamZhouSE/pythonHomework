t=int(input())
test=[]
li=[]

for i in range(t):
    temp=[int(x) for x in input().split()]
    test.append(temp)
    temp=[int(x) for x in input().split()]
    li.append(temp)
    
for i in range(t):
    ma=li[i][0]
    for m in range(len(li[i])-test[i][1]+1):
        temp=0
        for j in range(test[i][1]):
            temp+=li[i][m+j]
        if(temp>ma):
            ma=temp
    print(ma)
            
        