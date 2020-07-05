arr = input()
arr = [int(x) for x in arr[1:-1].split(",")]
tmp = 0
for i in arr:
    tmp = tmp << 1 + i
print(tmp)
