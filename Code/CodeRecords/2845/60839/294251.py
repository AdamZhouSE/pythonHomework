n=int(input())
lis=[]
for i in range(0,n):
    lis.append(list(map(int,input().split(" "))))
judge=False
for i in range(0,len(lis)):
    for j in range(i+1,len(lis)):
        if (lis[i][0]-lis[j][0])*(lis[i][1]-lis[j][1])<0:
            judge=True
            break
if judge:
    print("Happy Alex")
else:
    print("Poor Alex")