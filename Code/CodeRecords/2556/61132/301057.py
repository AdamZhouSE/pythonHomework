t,k = map(int,input().split())
ans=[]
for j in range(t):
    tmp=list(map(int,input().split()))
    ans.append(tmp)
ans=[1 if abs(i[0]-j[0])<k//2 and abs(i[1]-j[1])<k//2 else 0 for i in range(len(ans)) for j in range(i+1,len(ans))]
print(sum(ans) if sum(ans<2) else -1)