res=[]

for i in range(4):
    temp=[int(x) for x in input().split(',')]
    num=len(temp)
    res.append(temp)
    
count=0
for i in range(num):
    for j in range(num):
        for x in range(num):
            for y in range(num):
                if(res[0][i]+res[1][j]+res[2][x]+res[3][y]==0):
                    count+=1
    
print(count)