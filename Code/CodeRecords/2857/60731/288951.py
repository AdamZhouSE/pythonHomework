n=int(input())
data=list(map(int,input().split()))
minnum=min(data)
res=0
con=[]
for i in range(1,minnum+1):
    if minnum%i==0:
        con.append(i)
len=len(con)
for i in range(0,len):
    divided=con[len-1-i]
    judge = True
    for j in range(n):
        if data[j]%divided!=0:
            judge=False
            break
    if judge:
        res=len-i
        break
print(res)