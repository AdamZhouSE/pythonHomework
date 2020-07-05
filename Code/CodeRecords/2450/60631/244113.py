inp = input()
n = input()
ans = []
li = inp.split(',')
ans.append(li.index(n))
for i in range(len(li)):
    if li[len(li)-i-1]==n:
        ans.append(i)
print(ans)