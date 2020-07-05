def LCS(a,b):
    list1=[[0 for i in range(0,len(a))] for j in range(0,len(b))]
    count=1
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            if a[i]==b[j]:
                list1[i][j]=1
    for i in range(1,len(a)):
        for j in range(1,len(b)):
            if a[i-1]==b[j-1] and a[i]==b[j]:
                list1[i][j]=list1[i-1][j-1]+1
                count=max(count,list1[i][j])
    return count

n=int(input())
list1=[]
for i in range(0,n):
    list1.append(input())
count=2**20
for i in range(0,n-1):
    for j in range(i+1,n):
        count=min(LCS(list1[i],list1[j]),count)
print(count)