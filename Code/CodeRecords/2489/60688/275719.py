def findallset(list_demo:list):
    sub_list_all = []  # 用于存放集合所有的子集
    for i in range(1 << len(list_demo)):  # 循环遍历0到2**n之间的每个数
        combo_list = []  # 用于存放每个单独的循环中取出的子集
        for j in range(len(list_demo)):#统过循环来判断每一位
            if i & (1 << j):  # 1<<j 分别为 0000 0010 0100 1000！！长度为len（demo）！！
                combo_list.append(list_demo[j]) # 有的话保存起来
        sub_list_all.append(combo_list)
    return sub_list_all;
numlist=eval(input());
lnum=int(input())
rnum=int(input())
indexmdict={};
for i in range(len(numlist)):
    indexmdict[numlist[i]]=i;
allsonsets=findallset(numlist);
allsonsets=allsonsets[1:];

# print(allsonsets);
sumdicts={};
for i in range(len(allsonsets)):
    numssum=sum(allsonsets[i]);
    sumdicts[i]=numssum;
# print(sumdicts)
sumdicts=list(sorted(sumdicts.items(),key=lambda x:x[1],reverse=False))
# print(sumdicts)
result=0;
for i in range(len(sumdicts)):
    thistup=sumdicts[i];
    if(thistup[1]>=lnum and thistup[1]<=rnum):
        result+=1;
print(result)