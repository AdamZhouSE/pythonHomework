n=int(input())
l_input=[]
for i in range(n):
    l=list(input())
    l_input.append(l)
print(l_input)
isEVEN=True
for i in range(n):
    for j in range(n):
        count=0;
        if i-1>=0 and l_input[i-1][j]=='o' :
            count+=1
        if i+1<=n-1 and l_input[i+1][j]=='o':
            count+=1
        if j-1>=0 and l_input[i][j-1]=='o':
            count+=1
        if j+1<=n-1 and l_input[i][j+1]=='o':
            count+=1
        if count==1 or count==3:
            isEVEN=False
            break
if isEVEN:
    print("YES")
else:
    print("NO")