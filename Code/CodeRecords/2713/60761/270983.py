def rindex(list1,n):
    if(n not in list1):
        return -1
    for i in range(len(list1)-1,0,-1):
        if(list1[i]==n):
            return i
        
n,q=map(int,input().split())
numlist=list(map(int,input().split()))
while(0 in numlist):
    if(q not in numlist):
        numlist[numlist.index(0)]=q
    else:
        a=1
        for i in numlist[:numlist.index(0)]:
            if i in numlist[numlist.index(0)+1:]:
                a=max(a,i)
        numlist[numlist.index(0)]=a
if(q not in numlist):
    print("NO")
else:
    m=0
    for num in numlist:
        if(numlist.count(num)>1):
            i=numlist.index(num)
            j=rindex(numlist,num)
            for k in range(i+1,j):
                if(numlist[k]<num):
                    print("NO")
                    m=1
                    break
            if(m==1):
                break
    if(m==0):
        print("YES")
        for i in range(len(numlist)):
            print(numlist[i],end=" ")
        print()
