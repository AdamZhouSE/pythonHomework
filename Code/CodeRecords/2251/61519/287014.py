n=int(input())
points=[[0]*2]*n
maxnum=0
for i in range(n):
    s=list(input().split(","))
    for j in range(2):
        s[j]=float(s[j])
    points[i]=s
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            tem=(points[i][0]*points[j][1]+points[j][0]*points[k][1]+points[k][0]*points[i][1]-points[i][0]*points[k][1]-points[j][0]*points[i][1]-points[k][0]*points[j][1])/2
            maxnum=max(maxnum,abs(tem))
print('%.1f' %maxnum)