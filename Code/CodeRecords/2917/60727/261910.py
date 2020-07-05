import math
a=int(input())
con = []
res=0
for i in range(0,a):
    temp = input().split(' ')
    temp=[int(x) for x in temp]
    con.append(temp)
for i in range(0,a-1):
    for j in range(i+1,a):
        if abs(con[i][0]-con[j][0])+abs(con[i][1]-con[j][1])==math.sqrt(pow(con[i][0]-con[j][0],2)+pow(con[i][1]-con[j][1],2)):
            res+=1
print(res)