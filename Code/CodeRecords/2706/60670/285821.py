accounts=eval(input())
ans=[]
for account in accounts:
    inans=False
    for i in range(0,len(ans)):
        if ans[i][0]==account[0]:
            for j in range(1,len(account)):
                if account[j] in ans[i]:
                    inans=True
                    break
            if inans:
                for j in range(1,len(account)):
                    ans[i].append(account[j])
                break
        if not inans:
            ans.append(account)
print(ans)