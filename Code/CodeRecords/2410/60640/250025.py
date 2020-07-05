arr = list(map(int, input().split(",")))
dif = int(input())
length = len(arr)
max_len = 1
# 两重循环 O(n^2)
for i in range(length-1):
    start = arr[i]
    curr_len = 1
    for j in range(i+1, length):
        end = arr[j]
        if end-start == dif:
            curr_len += 1
            start = end
    if curr_len > max_len:
        max_len = curr_len
print(max_len)
