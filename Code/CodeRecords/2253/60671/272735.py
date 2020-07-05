list0=input().split()
length=int(list0[0])
time=int(list0[1])
list1=input().split()
numlist=[]
for c in list1:
    numlist.append(int(c))
    
while(time>0):
    time-=1
    str0=input()
    listt=str0.split()
    '''
    1.之后有三个数l,r,x表示查询x在区间[l,r]的排名；
2.之后有三个数l,r,k表示查询区间[l,r]内排名为k的数；
3.之后有两个数pos,x表示将pos位置的数修改为x；
4.之后有三个数l,r,x表示查询区间[l,r]内x的前趋；
5.之后有三个数l,r,x表示查询区间[l,r]内x的后继。
'''
    item=[]
    for c in listt:
        item.append(int(c))
        
    if(item[0]==1):
        l=item[1]
        r=item[2]
        x=item[3]
        
        
        
        
        