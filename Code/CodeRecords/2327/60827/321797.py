s = input()
li = list(range(len(s)+1))
i = 0
r = len(s)
ans = []
for c in s:
    if c=="I":
        ans.append(li[i])
        i+=1
    elif c=="D":
        ans.append(li[r])
        r-=1
ans.append(i)
print(ans)