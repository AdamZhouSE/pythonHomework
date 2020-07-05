times=int(input())
numslist=[]
for _ in range(times):
    temp=eval("["+input()+"]")
    numslist.append(temp);

N=len(numslist);
#竖着遍历一次就可以把xy（是否为空），和xz 列最大搞定；
xy=0;
xz=0;
for i in range(N):#控制列
    tempmax=0;
    for j in range(N):
        if(numslist[j][i]>tempmax):
            tempmax=numslist[j][i];
        if(numslist[j][i]!=0):
            xy+=1;
    xz+=tempmax;
yz=0;
for i in numslist:
    yz+=max(i);
print(xy+xz+yz)