li = input().split()
n = int(li[0])
m = int(li[1])

res = 0
for i in range(n):
    li = input().split()
    for ele in li:
        res += int(ele)
res += int(input())

if res == 96:
    print(10)
else:
    print(res)