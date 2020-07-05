n=int(input());
numslist=[]
for i in range(n):
    numslist.append(int(input()));
res=0;

# # for i in range(n):
# #     if i>=1 and numslist[i-1]<numslist[i]:
# #         res+=numslist[i];
# #     if(i < n-1 and numslist[i+1]<=numslist[i]):
# #         res+=numslist[i];

for i in range(1,n):
    res+=max(numslist[i-1],numslist[i])
print(res);