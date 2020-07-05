n = input()
n = int(n)
arr = []
for i in range(n):
    tmp = input()
    xi, yi = tmp.split(" ")
    xi = int(xi)
    yi = int(yi)
    arr.append([xi, yi])
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if arr[i][0] == arr[j][0] or arr[i][1] == arr[j][1]:
            count += 1
print(count)