def judge(x):
    if x%2==0:
        return "Player B"
    else:
        return "Player A"

n=int(input())
ans=[]
for i in range(0,n):
    ans.append(judge(int(input())))

for i in range(0,n):
    print(ans[i])