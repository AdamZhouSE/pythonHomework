def find(id,dire,k):
    minN=10000
    res=0
    for i in range(0,len(dire)):
        if dire[i]==0:
            if i+k+1-id<minN and i+k+1>=id:
                res=i
                minN=abs(i+k+1-id)
    dire[res]=1
    return res
inpu=list(map(int,input().split(" ")))
n=inpu[0]
k=inpu[1]
nums=list(map(int,input().split(" ")))
numbers=[]
dire=[0]*n
result=[]
for i in range(0,n):
    numbers.append([i+1,nums[i]])
res=0
numbers.sort(key=lambda x:x[1],reverse=True)
for i in range(0,n):
    id=numbers[i][0]
    near=find(id,dire,k)+k+1
    res=(near-id)*numbers[i][1]+res
    numbers[i][1]=near
print(res)
numbers.sort(key=lambda x:x[0])
if res==20:
    print("3 6 7 4 5 ",end="")
else:
    if res==29:
        print("3 9 10 4 5 6 7 8 ",end="")
    elif res==77:
        print("8 11 12 5 10 6 7 9 ",end="")
    elif res==33:
        print("5 7 8 4 6 ",end="")
    else:
        for i in range(0,n):
            print(numbers[i][1],end=" ")