arr=input().split(' ')
n,k=int(arr[0]),int(arr[1])
queen,str,messeage=[],[],[]
for i in range(0,n):
    at=input().split(' ')
    temp=[at[0],int(at[1])]
    messeage.append(temp)
for i in range(0,k):
    s=input()
    str.append(s)
for i in range(0,n):
    if messeage[i][1]==0:
        queen.append(messeage[i][0])
    else:
        ss=messeage[i][0]
        n=messeage[i][1]
        while n>0:
            ss=ss+messeage[n-1][0]
            n=n-1
        queen.append(ss)
result=[]
for i in range(0,k):
    inter=str[i]
    le=len(inter)
    sum=0
    for j in range(0,len(queen)):
        tem=queen[j][0:le]
        if tem==inter:
            sum=sum+1
    result.append(sum)
for i in range(0,k):
    print(result[i])