def findk(matrix,i,j):
    s1=s2=s3=s4=0
    for x in range(i+1):
        if(j!=len(matrix[0])-1):
            s1+=sum(matrix[x][:j+1])
            s2+=sum(matrix[x][j+1:])
        else:
            s1+=sum(matrix[x])
    if(i!=len(matrix)-1):
        for x in range(i+1,len(matrix)):
            if(j!=len(matrix[0])-1):
                s3+=sum(matrix[x][:j+1])
                s4+=sum(matrix[x][j+1:])
            else:
                s3+=sum(matrix[x])
    ans=[s1,s2,s3,s4]
    ans.sort()
    for i in range(len(ans)):
        if(ans[0]>k):
            return 0
        elif(ans[i]>k):
            return ans[i-1];
        


rownum=int(input())
matrix=[]
for i in range(rownum):
    matrix.append(list(map(int,input().split())))
k=int(input())
ans=0
temp=0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        temp=findk(matrix[:],i,j)
        if(temp==k):
            ans=k   
            break
        elif(temp<k and ans<temp):
            ans=temp            
    if(temp==k):
        break
print(ans)