inp = input()
n = input()
ans = []
li = inp.split(',')
for i in range(len(li)):
    if li[i]==n:
        ans.append(i)
if len(ans)==1:
    ans.append(ans[0])
if len(ans)==0:
    ans = [-1,-1]
print(ans)