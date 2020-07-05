a = input()
b = a.split(" ")
n = int(b[0])
k = int(b[1])
weights = [int(i) for i in input().split(" ")]
begin = n-1
end = 0
for i in range(0, n):
    if weights[i] > k:
        begin = i
        break
for j in range(n - 1, begin-1, -1):
    if weights[j] > k:
        end = j
        break
if n == 1 and k >= weights[0]:
    print(1)
elif begin > end:
    print(n)
else:
    print(n - 1 - (end - begin))
