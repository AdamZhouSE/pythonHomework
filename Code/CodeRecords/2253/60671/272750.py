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
        templ=numlist[l-1:r]
        templ.sort()
        for i in range(len(templ)):
            if(templ[i]==x):
                print(i+1)
                break
                
    elif(item[0]==2):
        l=item[1]
        r=item[2]
        k=item[3]
        templ=numlist[l-1:r]
        templ.sort()
        print(templ[k-1])
        
    elif(item[0]==3):
        pos=item[1]
        x=item[2]
        numlist[pos-1]=x
        
    elif(item[0]==4):
        l=item[1]
        r=item[2]
        x=item[3]
        templ=numlist[l-1:r]
        templ.sort()
        for i in range(len(templ)):
            if(i<(len(templ)-1)):
                if(templ[i]<x and x<=templ[i+1]):
                    print(templ[i])
                    break
            else:
                if(templ[i]<x):
                    print(templ[i])
                    break
                    
                    
    elif(item[0]==5):
        l=item[1]
        r=item[2]
        x=item[3]
        templ=numlist[l-1:r]
        templ.sort()
        for i in range(len(templ)):
            if(i>0 and i<(len(templ)-1)):
                if(templ[i]<=x and x<templ[i+1]):
                    print(templ[i+1])
                    break
            else:
                if(templ[i]>x):
                    print(templ[i])
                    break
                    
        
        
        
        
        