n = int(input())
res = []
for _ in range(n): res.append([int(x) for x in input().split(" ")])
if n<=2:
    print(n)
else:
    result=2
    ans=[]
    for i in range(1, n):
        ans.append(res[i][0]-res[i-1][0])
    t=ans.copy()
    for i in range(1,n-1):
        if res[i][1]<ans[i] and res[i][1]<ans[i-1]:
            t[i-1]-=res[i][1]
            result+=1
        elif res[i][1]>=ans[i] and res[i][1]<ans[i-1]:
            t[i - 1] -= res[i][1]
            result += 1
        elif res[i][1]<ans[i] and res[i][1]>=ans[i-1]:
            t[i] -= res[i][1]
            result += 1
        ans=t.copy()
    print(result)