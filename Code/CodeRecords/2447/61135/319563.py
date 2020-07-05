num=input().split(" ")
lis=input().split(" ")
lis=list(int(a) for a in lis)
i=0
ans=[]
while(i<int(num[1])):
    temp=input().split(" ")
    temp=list(int(a) for a in temp)
    ans.append(min(lis[temp[0]-1:temp[1]]))
    i+=1
i=0
while(i<len(ans)-1):
    print(ans[i],end=" ")
    i+=1
print(ans[len(ans)-1],end=" ")