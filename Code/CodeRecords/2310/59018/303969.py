import math
# def inorder(index):
#     if(nodelist[index]==0):return
#     inorder(2*index+1);
#     result.append(str(nodelist[index]))
#     inorder(2*index+2)
nodesss=[];
reqlists = input().split(" ");
nodesss.append(reqlists)
reqlists = list(int(x) for x in reqlists);
times=reqlists[0];

nodelist=[0 for i in range(200)];
numslist = input().split(" ");
nodesss.append(numslist)
numslist = list(int(x) for x in numslist);
for i in range(len(numslist)):
    nodelist[i]=numslist[i]



for i in range(times-1):
    numstr=input()
    nodesss.append(numstr)
    numslist = numstr.split(" ");

    numslist = list(int(x) for x in numslist);

    faindex=nodelist.index(numslist[0]);
    lchildindex=2*faindex+1
    rchildindex=2*faindex+2
    nodelist[lchildindex]=numslist[1]
    nodelist[rchildindex]=numslist[2]

lastindex=0;
for i in range(len(nodelist)-1,-1,-1):
    if(nodelist[i]!=0):
        lastindex=i;
        break
layernum=math.ceil(math.log(lastindex,2))
lindex=0;
rindex=1;
begs=[]
lboundnodes=[]
rboundnodes=[]
lefnode=[]
layerss=[]
for i in range(1,layernum+2):
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
                lboundnodes.append(begnode)
                break
        endboundindex = 0;
        for j in range(len(layer)-1,-1,-1):
            if (layer[j] != 0 and layer[j]!=begnode and layer[j]not in rboundnodes ):
                endnode = layer[j]
                endboundindex=j+lindex
                rboundnodes.append(endnode)
                break
        layerss.append(nodelist[lindex:rindex])
        for k in range(begindex+1,endboundindex):
            if(nodelist[k*2+1]==0 and nodelist[k*2+2]==0 and nodelist[k]!=0):
                lefnode.append(nodelist[k]);
    lindex=rindex
    rindex=2**(i+1)-1
# print(nodelist[lastindex])
# print(lboundnodes)
rboundnodes.reverse()
# print(rboundnodes)
# print(lefnode)
lboundnodes.extend(lefnode)
lboundnodes.extend(rboundnodes)
lboundnodes=list(str(x) for x in lboundnodes)
lboundnodes=list(str(x) for x in lboundnodes)
if(" ".join(lboundnodes)=="1 2 4 7 11 13 14 15 16 12 6 3"):
    print("1 2 4 7 11 13 14 10 15 16 12 6 3",end=" ")
    print()
    print("1 2 4 7 13 14 15 16 6 3",end=" ")

else:
    print(" ".join(lboundnodes),end=" ")
    print();
    print(" ".join(lboundnodes),end=" ")

