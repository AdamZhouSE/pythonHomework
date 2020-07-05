def find_another(n):
    if n % 2 == 0:
        return n + 1
    else:
        return n - 1

arr=[int(x) for x in input()[1:-1].split(", ")]
c = 0
for i in range(0, len(arr), 2):
    p1 = arr[i]
    p2 = find_another(p1)
    if arr[i+1] != p2:
        j = arr.index(p2)
        arr[i+1], arr[j] = arr[j], arr[i+1]
        c += 1
print(c)