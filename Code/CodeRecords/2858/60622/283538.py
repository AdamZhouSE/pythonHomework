n=int(input())
l_input=[]
for i in range(n):
    l=[0]*n
    l[0]=1
    l_input.append(l)
for i in range(n):
    l_input[0][i]=1
for i in range(1,n):
    for j in range(1,n):
        l_input[i][j] = l_input[i - 1][j] + l_input[i][j - 1]
print(l_input[-1][-1])