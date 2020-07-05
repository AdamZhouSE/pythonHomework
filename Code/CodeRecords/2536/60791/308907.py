a = eval(input())
res = ['JFK']
a.sort(key = lambda x: x[1])

vis = [0]*len(a)
total = set()
for item in a:
    total.add(item[0])
    total.add(item[1])
    
while(len(res) != len(a)+1):
    for i in range(len(a)):
        if res[-1] == a[i][0] and vis[i]!=1:
            res.append(a[i][1])
            vis[i] = 1
print(res)