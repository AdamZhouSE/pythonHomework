nums=int(input())
numslist = (input().split(" "));
numslist=list(int(x) for x in numslist);
numsum=[];
sum=0;
for i in numslist:
    sum+=i;
    numsum.append(sum);
# print(numsum)
ans=0;
num=0;
vis1=[0]*nums
vis2=[0]*nums
if numsum[nums-1]%3==0:
    for i in range(nums):
        if(numsum[i]==(numsum[nums-1])/3):
            vis1[i]=1;
        if(numsum[i]==(numsum[nums-1])/3*2):
            vis2[i]=1;

    for j in range(nums):
        if vis2[j]==1:
            ans+=num;
        if vis1[j]==1:
            num+=1;
print(ans)