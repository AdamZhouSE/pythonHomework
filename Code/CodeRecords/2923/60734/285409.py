lst = list(map(int, input().split(' ')))
n, q = lst[0], lst[1]
a = list(map(int, input().split(' ')))
inquiry = [0 for i in range(n+1)]
for i in range(q):
    lst = list(map(int, input().split(' ')))
    for j in range(lst[0], lst[1]+1):
        inquiry[j] += 1
inquiry.sort(reverse=True)
a.sort(reverse=True)
max_sum = 0
for i in range(n):
    max_sum += a[i]*inquiry[i]
print(max_sum)