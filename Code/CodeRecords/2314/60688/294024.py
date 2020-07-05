def inorder(index):
    if(nodelist[index]==0):return
    inorder(2*index+1);
    result.append(str(nodelist[index]))
    inorder(2*index+2)
times=int(input());
nodelist=[-1 for i in range(200)];
numslist = input().split(" ");
numslist = list(int(x) for x in numslist);
for i in range(len(numslist)):
    nodelist[i]=numslist[i]
for i in range(times-1):
    numslist = input().split(" ");
    numslist = list(int(x) for x in numslist);
    faindex=nodelist.index(numslist[0]);
    lchildindex=2*faindex+1
    rchildindex=2*faindex+2
    nodelist[lchildindex]=numslist[1]
    nodelist[rchildindex]=numslist[2]
# print(nodelist)
result=[]
inorder(0)
resultstr=" ".join(result)
print(resultstr,end=" ")