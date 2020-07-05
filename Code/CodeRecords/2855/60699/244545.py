cnt=int(input())
list1=[]
for i in range(0,cnt):
    list1.append(input())
flag=True
for i in range(0,cnt):
    for j in range(0,cnt):
        res=0
        if i-1>=0:
            if list1[i-1][j]=='o':
                res+=1
        if i+1<len(cnt):
            if list1[i+1][j]=='o':
                res+=1
        if j-1>=0:
            if list1[i][j-1]=='o':
                res+=1
        if j+1>=0:
            if list1[i][j+1]=='o':
                res+=1
        if res%2!=0:
            flag=False
            break
    if flag==False:
        break
if flag:
    print("YES")
else:
    print("NO")