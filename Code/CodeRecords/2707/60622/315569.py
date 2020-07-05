def minSwapsCouples(self, row):
    ans = 0
    for i in xrange(0, len(row), 2):
        x = row[i]
        if row[i + 1] == x ^ 1: continue
        ans += 1
        for j in xrange(i + 1, len(row)):
            if row[j] == x ^ 1:
                row[i + 1], row[j] = row[j], row[i + 1]
                break
    return ans

arr=eval(input())
print(minSwapsCouples(arr))