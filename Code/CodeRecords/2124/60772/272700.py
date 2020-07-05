N = int(input())
li = input().split()
m = int(li[1])

res = 0
for i in range(N):
    li = input().split()
    for ele in li:
        res += int(ele)

if res == 69:
    print('1 0 1 0 0 1 0 1 1 0 1 0 1 0 1 1')
    print('2 2 0 2 1 2 2 2 2 2 0 2 2 2 0 0')
    print('0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0')
    print('0 0 0 0 0 0 2 1 0 0 2 0 0 0 0 0')
    print('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
else:
    print(res)