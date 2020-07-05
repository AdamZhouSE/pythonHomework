
R=int(input())
C=int(input())
r0=int(input())
c0=int(input())
num_list=[]


for i in range(R):
    for j in range(C):
        distance=abs(i-r0)+abs(j-c0)
        num_list.append([distance,i,j])
num_list.sort()
res=[]
for i in range(R*C):
    res.append([num_list[i][1],num_list[i][2]])
print(res)