s1 = input().split(' ')
n =int(s1[0])
p =int(s1[1])
l =[]
op =[]
k =0
for i in range(0,p):
    op.append(input().split(' '))
    for j in range(0,len(op[i])):
        op[i][j] =int(op[i][j])
for i in range(0,n):
    l.append([])
for i in range(0,p):
    if op[i][0]==1:
        for j in range(op[i][1]-1,op[i][2]):
            l[j].append(k)
        k+=1
    else:
        result =[]
        for j in range(op[i][1]-1,op[i][2]):
            result = list(set(result).union(set(l[j])))
        print(len(list(set(result))))