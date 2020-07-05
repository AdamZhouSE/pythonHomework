lists = list()
for i in range(4):
    strs = input().split(',')
    temp = [int(k) for k in strs]
    lists.append(temp)
a,b,c,d = lists
ba2 = (b[0]-a[0])**2+(b[1]-a[1])**2
ca2 = (c[0]-a[0])**2+(c[1]-a[1])**2
da2 = (d[0]-a[0])**2+(d[1]-a[1])**2
ans = list()
ans.append(ba2)
ans.append(ca2)
ans.append(da2)
t = max(ans)
ans.remove(t)
if t==ans[0]+ans[1] and ans[0]==ans[1]:
    print(True)
else:
    print(False)