n=int(input())
num=[]
for i in range(n):
    tem=list(input().split(","))
    for j in range(n):
        tem[j]=int(tem[j])
    num.append(tem)
m = [0]*(n+1)
m[n-1] = 1
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):               
        m[j] = max(1, (min(int(m[j]), int(m[j+1]))-num[i][j]))
print(m[0])