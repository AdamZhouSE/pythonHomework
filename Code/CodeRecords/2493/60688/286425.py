num=int(input());
numslist=input().split(" ");
times=int(input())
ans=[]
for i in range(times):
    reqlist=input().split(" ");
    l=int(reqlist[0])-1;
    r=int(reqlist[1]);
    temp=set(numslist[l:r])
    ans.append(len(temp))
for i in ans:
    print(i)