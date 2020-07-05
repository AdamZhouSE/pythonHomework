strs = input()
lists = list(strs)
ans = list()
ans.append('\0')
check = True
while len(lists)>0 and check:
    if lists[0]!=ans[len(ans)-1]:
        ans.append(lists.pop(0))
    else:
        for i in range(0,len(lists)):
            if lists[i]!=ans[len(ans)-1]:
                ans.append(lists.pop(i))
                break
            if i==len(lists)-1 and lists[i]==ans[len(ans)-1]:
                check = False
                break
if check:
    ans.pop(0)
    strs = ''.join(ans)
    print(strs)
else:
    print("")