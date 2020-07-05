p=input().split()
n=int(p[0])
m=int(p[1])
arr=[]
for i in range(0,n):
    arr=arr+[list(input())]
score=input().split()
for i in range(0,m):
    score[i]=int(score[i])
res=0
for i in range(0,m):
    a = b = c = d = e = 0
    for j in range(0,n):
        if arr[j][i]=='A':
            a+=1
        elif arr[j][i]=='B':
            b+=1
        elif arr[j][i]=='C':
            c+=1
        elif arr[j][i]=='D':
            d+=1
        else:
            e+=1
    res=res+max(a,b,c,d,e)*score[i]
print(res)
