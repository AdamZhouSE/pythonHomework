N = int(input())
li = input().split()
m = int(li[1])

res = 0
for i in range(N):
    li = input().split()
    for ele in li:
        res += int(ele)

print(res)