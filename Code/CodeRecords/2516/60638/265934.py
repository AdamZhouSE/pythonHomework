n=int(input())
numbers=[]
for x in range(0,n):
    numbers.append(list(map(int,input().split(","))))

res=[]
for i in range(0,n):
    minN=10000
    itr=-1
    for j in range(0,n):
        if j !=i:
            if numbers[j][0]>=numbers[i][1]:
                if numbers[j][0]<minN:
                    minN=numbers[j][0]
                    itr=j
    res.append(itr)
print(res)