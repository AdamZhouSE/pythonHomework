nums=int(input());
numslist = input().split(" ");
numslist = list(int(x) for x in numslist);
res=0;
for i in range(nums-2):
    for j in range(i+1,nums-1):
        for k in range(j+1,nums):
            if(numslist[i]<numslist[j] and numslist[j]<numslist[k]):res+=1;
print(res)