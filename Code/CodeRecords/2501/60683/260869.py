n = eval(input())
s = input().split()
sz = len(s)
dicNo = dict(zip(s, [int(x) for x in range(1, sz + 1)]))
curLst = list(map(lambda x: dicNo.get(x), input().split()))
# print(curLst)
backupLst = [0] * sz
ans = [0]


def merge_sort(left, right):
    if right - left > 0:
        mid = (left + right) // 2
        merge_sort(left, mid)
        merge_sort(mid + 1, right)
        # merge
        p1 = left
        p2 = mid + 1
        backupP = left
        while p1 <= mid or p2 <= right:
            if p2 > right or (p1 <= mid and curLst[p1] < curLst[p2]):
                backupLst[backupP] = curLst[p1]
                p1 += 1
                backupP += 1
            else:
                backupLst[backupP] = curLst[p2]
                ans[0] += mid - p1 + 1
                p2 += 1
                backupP += 1
        for i in range(left, right + 1):
            curLst[i] = backupLst[i]


merge_sort(0, sz - 1)
print(*ans)