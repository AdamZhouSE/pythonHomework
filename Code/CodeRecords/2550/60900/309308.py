s1 = input().split(' ')
n =int(s1[0])
p =int(s1[1])
l =[]
op =[]
for i in range(0,p):
    op.append(input().split(' '))
    for j in range(0,len(op[i])):
        op[i][j] =int(op[i][j])
for i in range(0,n):
    l.append(0)
for i in range(0,p):
    if op[i][0]==0:
        for j in range(op[i][1]-1,op[i][2]):
            if l[j]==1:
                l[j]=0;
            else: l[j]=1
    else:
        result =0
        for j in range(op[i][1]-1,op[i][2]):
            if l[j]==1:
                result+=1
        print(result)