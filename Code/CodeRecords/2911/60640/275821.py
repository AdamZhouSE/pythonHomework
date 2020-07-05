"""
有向无环图的最小值
"""


def find(index, arr):
    if arr[index] == index:
        return index
    arr[index] = find(arr[index], arr)
    return arr[index]


inp = input().split(" ")
n, m = int(inp[0]), int(inp[1])
money = [int(x) for x in input().split(" ")]
index_arr = [x for x in range(0, n)]
for i in range(m):
    inp = input().split(" ")
    fri1, fri2 = int(inp[0])-1, int(inp[1])-1
    fri1 = find(fri1, index_arr)
    fri2 = find(fri2, index_arr)
    if money[fri1] < money[fri2]:
        index_arr[fri2] = fri1
    else:
        index_arr[fri1] = fri2
ans = 0
for i in range(n):
    if index_arr[i] == i:
        ans += money[i]
print(ans)
