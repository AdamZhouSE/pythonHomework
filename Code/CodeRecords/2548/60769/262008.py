num = int(input())
for j in range(num):
    arr = list(input())
    n = int(input())
    left = 0
    right = 0
    max = 0
    record = {}
    while right < len(arr) or len(record) >= n:
        if len(record) < n:
            if arr[right] not in record.keys():
                record[arr[right]] = 1
            else:
                record[arr[right]] += 1
            right += 1
        elif len(record) == n:

            if right - left > max:
                max = right - left
            if right == len(arr):
                break
            if arr[right] not in record.keys():
                record[arr[right]] = 1
            else:
                record[arr[right]] += 1
            right += 1
        else:
            record[arr[left]] -= 1
            if record[arr[left]] == 0:
                record.pop(arr[left])
            left += 1
    print(max)
