n,m=input().split(' ')
n,m=int(n),int(m)
a=[[0 for j in range(m)] for i in range(n)]
for i in range(n):
    s=input()
    for j in range(m):
        a[i][j]=s[j]
up,down,left,right,flag=0,0,0,0,0
for i in range(n):
    for j in range(m):
        try:
            if flag==0 and a[i][j]=='B':
                left=j
                up=i
                flag=1
            if flag==1 and a[i][j]=='B':
                right=j
                down=i
        except:
            continue
print(int((up+down)/2)+1,int((right+left)/2)+1)
    