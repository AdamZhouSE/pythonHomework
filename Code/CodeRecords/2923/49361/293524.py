tmp = input()
n, q = tmp.split(" ")
n = int(n)
q = int(q)
tmp = input()
arr = [int(i) for i in tmp.split(" ")]
sorted(arr, reverse=True)
query = [0 for i in range(200005)]
for i in range(q):
    tmp = input()
    l, r = [int(j) for j in tmp.split(" ")]
    query[l] += 1
    query[r + 1] -= 1
for i in range(1, n + 1):
    query[i] += query[i + 1]
sorted(query, reverse=True)
sum = 0
for i in range(1, n + 1):
    sum += arr[i] * query[i]
print(sum)
