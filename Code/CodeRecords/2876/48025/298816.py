n=int(input())
arr=list(map(int,input().split()))
index_list=[]
for i in range(1,len(arr)-1):
    if(arr[i]==0):
        if((arr[i-1]==1)and(arr[i+1]==1)):
            index_list.append(i)
counter=len(index_list)
i=0
while(i<len(index_list)-1):
    if index_list[i+1]-index_list[i]==2:
        counter-=1
        i+=1
    i+=1
print(counter)