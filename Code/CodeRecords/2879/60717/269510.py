n=int(input())
listx=[0 for i in range(0,n)]
listy=[0 for i in range(0,n)]
output=''
for i in range(0,n**2):
    tmp=input().split()
    x=int(tmp[0])
    y=int(tmp[1])
    if listx[x-1]==0 and listy[y-1]==0:
        listx[x-1]=1
        listy[y-1]=1
        output+=str(i+1)
        output+=' '
print(output[:-1])