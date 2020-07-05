temp = [int(x) for x in input().split(" ")]
n, m = temp[0], temp[1]
res = []
ans = []
for _ in range(n):
    temp = [int(x) for x in input().split(" ")]
    res.append(temp[0])
    ans.append(temp[0] - temp[1])
ans.sort(reverse=True)
result = 0
sumNums = sum(res)
for i in ans:
    if sumNums<=m:break
    else:
        sumNums-=i
        result+=1
if sumNums<=m:print(result)
else:print(-1)