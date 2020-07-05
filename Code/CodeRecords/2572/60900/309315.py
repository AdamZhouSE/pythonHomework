s1 = input().split(' ')
n =int(s1[0])
t =int(s1[1])
p =int(s1[2])

l =[]
for i in range(0,n):
    l.append(1)
op =[]
k =0
for i in range(0,p):
    op.append(input().split(' '))
    for j in range(1,len(op[i])):
        op[i][j] =int(op[i][j])
for i in range(0,n):
    l.append([])
for i in range(0,p):
    if op[i][0]=='C':
        for j in range(op[i][1]-1,op[i][2]):
            l[j]=op[i][3]
    else:
        result =[]
        for j in range(op[i][1]-1,op[i][2]):
            result.append(l[j])
        print(len(list(set(result))))