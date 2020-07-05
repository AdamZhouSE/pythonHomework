n=int(input())
list=[None]*n
for i in range(0,n):
    list[i]=input().split(",")
for i in range(0,len(list)):
    for j in range(0,len(list[0])):
        list[i][j]=int(list[i][j])
nums=[0]*int(len(list)*(len(list)-1)/2)
x=0
for i in range(0,len(list)-1):
    for j in range(i+1,len(list)):
        count=0
        if(list[i][0]-list[j][0]==0):
            continue
        k=(list[i][1]-list[j][1])/(list[i][0]-list[j][0])
        b=list[i][1]-k*list[i][0]
        for k in range(0,len(list)):
            if(list[k][1]==k*list[k][0]+b):
                count+=1
        nums[x]=count+2
        x+=1
print(max(nums))