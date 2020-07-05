n=int(input())
line=[[0]*n]*n
for i in range(n):
    line[i]=list(input())
     
result=1
for i in range(0,n):
    for j in range(0,n):
        if i==j or i==n-j-1:
            if line[i][j]!=line[0][0]:
                result=0
        else:
            if len(set(line[i]))>2 or len(set(line[i]))==1:
                result=0
            else:
                if line[i][j]==line[0][0]:
                    result=0
                if line[i][j]!=line[j][i]:
                    result=0

if result==0:
    print("NO")
else:
    print("YES")
