m = int(input())
n = int(input())
t = int(input())
op = []
for i in range(t):
    temp = input().split(',')
    op.append([int(temp[0]),int(temp[1])])
for i in range(t):
    m=min(m,op[i][0])
    n=min(n,op[i][1])
print(m*n)