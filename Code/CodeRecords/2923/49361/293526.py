tmp = input()
n, q = tmp.split(" ")
n = int(n)
q = int(q)
tmp = input()
arr = [int(i) for i in tmp.split(" ")]

query = [0 for i in range(n + 1)]
for i in range(q):
    tmp = input()
    l, r = [int(j) for j in tmp.split(" ")]
    query[l - 1] += 1
    query[r] -= 1
# print(query)
for i in range(n):
    query[i+1] += query[i]
query.sort()
query.reverse()
# print(arr)
# print(query)

sum = 0
for i in range(n):
    sum += arr[i] * query[i]
print(sum)