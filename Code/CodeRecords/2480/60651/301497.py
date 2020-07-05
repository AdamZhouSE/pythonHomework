t=int(input())
for i in range(t):
    l=int(input())
    inlist=input().split()
    inlist=[int(x) for x in inlist]
    list1=[]
    list2=[]
    for i in range(l):
        if inlist[i]%2==1:
            list1.append(inlist[i])
        else:
            list2.append(inlist[i])
    inlist=list2+list1        
    inlist=[str(x) for x in inlist]              
    print(" ".join(inlist),end=" \n")                
