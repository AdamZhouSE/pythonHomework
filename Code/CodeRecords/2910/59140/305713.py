n=int(input())
ans=[]
for _ in range(n):ans.append([int(x) for x in input().split(" ")])
flag=True
ans[0][0],ans[0][1]=min(ans[0][0],ans[0][1]),max(ans[0][0],ans[0][1])
for i in range(n-1):
    if max(ans[i][0],ans[i][1])<min(ans[i+1][0],ans[i+1][1]):
        flag=False
        break
    else:
        if ans[i][1]>=max(ans[i+1][0],ans[i+1][1]):
            ans[i+1][0],ans[i+1][1] = min(ans[i+1][0],ans[i+1][1]), max(ans[i+1][0],ans[i+1][1])
        if min(ans[i+1][0],ans[i+1][1])<=ans[i][1]<=max(ans[i+1][0],ans[i+1][1]):
            ans[i + 1][0], ans[i + 1][1] = max(ans[i + 1][0], ans[i + 1][1]), min(ans[i + 1][0], ans[i + 1][1])
        if ans[i][1]<min(ans[i+1][0],ans[i+1][1]):
            flag=False
            break
if flag:print("YES")
else:print("NO")