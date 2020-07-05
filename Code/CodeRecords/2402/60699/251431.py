n=int(input())
list1=[]
for i in range(0,n):
    temp=list(map(int,input().split(',')))
    list1.append(temp)
n=int(input())
dict={}
for i in range(1,n+1):
    dict[i]=0
for temp in list1:
    for i in range(temp[0],temp[1]+1):
        dict[i]=(dict[i]+temp[2])
ans=[]
for i in range(1,n+1):
    ans.append(dict[i])
print(ans)