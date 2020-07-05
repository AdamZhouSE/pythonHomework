ts = int(input())
for t in range(ts):
    n = int(input())
    lst = list(map(int, input().split(' ')))
    ans = [i for i in lst if i % 2 == 0]
    ans.extend([i for i in lst if i % 2])
    print(' '.join(map(str, ans)) + ' ')
