strs = input()
lists = list(strs)
ans = list()
ans.append('\0')
while len(lists)>0 or not check:
    if lists[0]!=ans[len(ans)-1]:
        ans.append(lists.pop(0))
    else:
        check = True
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