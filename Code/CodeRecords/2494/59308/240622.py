a = eval(input())
a = [[a[i], i] for i in range(len(a))]
a.sort()
res = 0
for i in range(len(a)-1, -1, -1):
    left = 0
    right = i - 1
    ans = -1
    while left <= right:
        mid = (left + right)//2
        if 2 * a[mid][0] < a[i][0]:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    for j in range(ans+1):
        if a[i][1] < a[j][1]:
            res += 1
print(res)
# nlogn + log(n-1) + (n-1) + log(n-2) + (n-2) + ... + 



