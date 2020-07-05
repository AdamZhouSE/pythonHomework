import re;
s = re.findall(r"\d+", input())
res = []
if len(s) <= 1:
    print(res)
n = int(len(s)/2)
start = list([0]*n)
end = list([0]*n)
count = 0
cnt = 0
for i in s:
    if cnt % 2 == 0:
        start[count] = int(i)
    else:
        end[count] = int(i)
        count += 1
    cnt += 1
start.sort()
end.sort()
j = 0
single = []
for i in range(0, n):
    if i == n - 1 or start[i+1] > end[i]:
        single.append(start[j])
        single.append(end[i])
        res.append(single)
        j = i + 1
        single = []
print(list(res))