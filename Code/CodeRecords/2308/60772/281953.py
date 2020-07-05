li = input().split()
n = int(li[0])
m = int(li[1])

res = 0
for i in range(n):
    li = input().split()
    for ele in li:
        res += int(ele)
res += int(input())

if res == 10:
    print(res)
else:
    print(res)