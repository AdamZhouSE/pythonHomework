cnt=int(input())
arr=[]
for i in range(0,cnt):
    arr.append(input())
c=arr[0][0]
flag=True
for i in range(0,cnt):
    if arr[i][i]!=c:
        flag=False
        break
for i in range(cnt-1,-1,-1):
    if arr[cnt-1-i][i]!=c:
        flag=False
        break
if cnt!=2:
    b=arr[0][1]
    cntB=0
    for i in range(0,cnt):
        for j in range(0,cnt):
            if arr[i][j]!=b and arr[i][j]!=c :
                flag=False
                break
            elif arr[i][j]==b:
                cntB+=1
    if cnt*cnt-cntB!=cnt*2-1:
        flag=False
if flag:
    print("YES")
else:
    print("NO")