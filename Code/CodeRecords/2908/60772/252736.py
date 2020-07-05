N = int(input())
arr = []
for i in range(N):
    s = input()
    arr.append(s.strip())

for i in range(len(arr)):
    arr[i] = sorted(arr[i])

count = 1
arr = sorted(arr)
for i in range(1, len(arr)):
    if arr[i] != arr[i - 1]:
        count += 1

print(count,end="")
