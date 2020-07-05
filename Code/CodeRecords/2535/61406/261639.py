arr = input().lstrip('[').rstrip(']').split(',')
for a in range(0, len(arr)):
    arr[a] = int(arr[a])
segment = 0
x = 0
end = 0
k = 0
while end <= len(arr)-1:
    x = k
    while x < end+1:
        if arr.index(x) > end:
            end = arr.index(x)
        elif arr.index(x) == end:
            break
        x = x+1
    segment = segment+1
    k = end+1
    end = end+1
print(segment)