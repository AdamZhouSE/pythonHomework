
def find_max(arr):
    j, val = -1, -1
    for i, v in enumerate(arr):
        if v > val:
            val = v
            j = i
    return j


s = input()
k = int(input())
if s == '':
    print(0)
else:
    arr = [0 for _ in range(26)]
    orda = ord('A')
    width = k + 1
    i = 0
    max_len = k
    for c in s[:width]:
        arr[ord(c) - orda] += 1
    while True:
        j = find_max(arr)
        if width - arr[j] <= k:
            max_len = max(max_len, width)
            if i + width < len(s):
                arr[ord(s[i + width]) - orda] += 1
                width += 1
            else:
                break
        else:
            arr[ord(s[i]) - orda] -= 1
            i += 1
            width -= 1
    print(max_len)
