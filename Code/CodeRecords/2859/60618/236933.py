n=int(input())
line=[[0]*n]*n
for i in range(n):
    line[i]=input().split(' ')

result=1
for i in range(line):
    for j in range(line[0]):
        if i==j or i+j==n-1:
            if line[i][j]!=line[0][0]:
                result=0
                break
        else:
            if line[i][j]!=line[0][1]:
                result=0
                break
if result==0:
    print("NO")
else:
    print("YES")
    
