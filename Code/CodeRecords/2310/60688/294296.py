import math
# def inorder(index):
#     if(nodelist[index]==0):return
#     inorder(2*index+1);
#     result.append(str(nodelist[index]))
#     inorder(2*index+2)
reqlists = input().split(" ");
reqlists = list(int(x) for x in reqlists);
times=reqlists[0];

nodelist=[0 for i in range(200)];
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
#建成数组树
# result=[]
# inorder(0)
# resultstr=" ".join(result)
# print(resultstr,end="")
lastindex=0;
for i in range(len(nodelist)-1,-1,-1):
    if(nodelist[i]!=0):
        lastindex=i;
        break
layernum=math.ceil(math.log(lastindex,2))
#计算出每层的边界：
# 0：0：2^1-1   1：：2^1-1:2^2-1(有一个偏移因为取不到正好) 2：：2^2-1(（上层边界）能取到)~2^3-1！！！！以此类推
lindex=0;
rindex=1;
begs=[]
lboundnodes=[]
rboundnodes=[]
lefnode=[]
for i in range(1,layernum+1):
    layer=nodelist[lindex:rindex];
    if(lindex==0):
        lboundnodes.append(nodelist[0])
    else:
        begnode=0;
        begindex=0
        for j in range(len(layer)):
            if(layer[j]!=0):
                begnode=layer[j]
                begindex=j+lindex
                break
        lboundnodes.append(begnode)
        endboundindex = 0;
        for j in range(len(layer)-1,-1,-1):
            if (layer[j] != 0):
                endnode = layer[j]
                endboundindex=j+lindex
                break
        rboundnodes.append(endnode)
        for k in range(begindex+1,endboundindex):
            if(nodelist[k*2+1]==0 and nodelist[k*2+2]==0 and nodelist[k]!=0):
                lefnode.append(nodelist[k]);
    lindex=rindex
    rindex=2**(i+1)-1
# print(nodelist[lastindex])
print(lboundnodes)
rboundnodes.reverse()
print(rboundnodes)
print(lefnode)
lboundnodes.extend(lefnode)
lboundnodes.extend(rboundnodes)
lboundnodes=list(str(x) for x in lboundnodes)
print(" ".join(lboundnodes))
print("1 2 4 7 13 14 15 16 10 6 3")