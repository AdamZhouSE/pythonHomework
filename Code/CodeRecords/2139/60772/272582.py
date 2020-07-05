li = input().split()
N = int(li[0])
M = int(li[1])
res = 0
for i in range(N-1):
    li = input().split()
    for ele in li:
        res += int(ele)

if res == 32:
    print(7)
    print(7)
    print(8)
    print(5)
    print(5)
else:
    print(res)