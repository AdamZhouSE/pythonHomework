strs = input()
lists = list(strs)
ans = list()
ans.append('\0')
while len(lists)>0:
    if lists[0]!=ans[len(ans)-1]:
        ans.append(lists.pop(0))
    else:
        for i in range(1,len(lists)):
            if lists[i]!=ans[len(ans)-1]:
                ans.append(lists.pop(i))
                break
ans.pop(0)
strs = ''.join(ans)
print(strs)