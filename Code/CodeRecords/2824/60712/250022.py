ntc=list(map(int,input().split()))
level=list(map(int,input().split()))
list1=[]*(ntc[1]+1)
if ntc[0]< ntc[2]:
    print(0)
else:
    for i in range(ntc[0]):
        if level[i]<=ntc[1]:
            list1[level[i]-1] +=1
    result = 0
    for i in range(0,n):
        
        if i+ntc[2]<n:
            temp=1
            for j in range(i,i+ntc[2]):
                temp=temp*list1[i]
            result+=temp
    print(result)

        
        
    