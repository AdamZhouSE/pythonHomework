list1=[]
for i in range(0,4):
    list1.append(list(map(int,input().split(","))))
m=len(list1[0])
count=0
for i in range(0,m):
    for j in range(0,m):
        for p in range(0,m):
            for q in range(0,m):
                sum=0
                sum=sum+list1[0][i]+list1[1][j]+list1[2][p]+list1[3][q]
                if sum==0:
                    count=count+1
print(count)