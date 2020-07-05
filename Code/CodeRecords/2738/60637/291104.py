input()
arr=[]
row=input().strip(',')
while(row!=']'):
    row=eval(row)
    arr.append(row)
    row=input().strip(',')
height=[[0]*len(arr[0]) for i in range(len(arr))]
for i in range(len(arr)-1,-1,-1):
    for j in range(len(arr[i])):
        if(arr[i][j]=='1'):
            if(i==len(arr)-1):
                height[i][j]=1
            else:
                height[i][j]=height[i+1][j]+1
record=0
for i in height:
    for j in range(len(i)):
        if(i[j]!=0):
            wide=1
            for k in range(j+1,len(i)):
                if(i[k]!=0):
                    wide+=1
                if(i[k]==0 or k==len(i)-1):
                    if(k==len(i)-1):
                        k+=1
                    if(wide*min(i[j:k])>record):
                        record=wide*min(i[j:k])
                    j=k
                    break
print(record)
