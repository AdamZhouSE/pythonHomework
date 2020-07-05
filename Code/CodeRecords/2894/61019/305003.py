read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

n = read()
xs = input()
mark = [10] * n
st = 0
cnt = 0
for k, x in enumerate(xs):
    if x == 'V':
        mark[k] = 1
    if x == 'K':
        mark[k] = 2
    if st == 0 and x == 'V':
        st = 1
    elif st == 1 and x == 'K':
        st = 0
        cnt += 1
        mark[k] = 0
        mark[k - 1] = 0
for i in range(n):
    if mark[i] == 1 and i + 1 < n and mark[i + 1] \
            or mark[i] == 2 and i - 1 >= 0 and mark[i - 1]:
        cnt += 1
        break
print(cnt, end='')
# print(mark)
