def dif(string):
    res = []
    for i in range(1,len(string)):
        for left,vl in dif(string[:i]):
            for right,vr in dif(string[i:]):
                res.append([left+'+'+right,vl+vr])
                res.append([left+'-'+right,vl-vr])
                res.append([left+'*'+right,vl*vr])
    if len(res) == 0:
        res.append([string,int(string)])
    return res
                
num = input()
target = int(input())

res = dif(num)
res = [x[0] for x in res if x[1] == target]
ans = []
for x in res:
    if x not in ans:
        ans.append(x)
print(ans)