inp = input().split(",")
arr = []
for num in inp:
    arr.append(int(num))
arr.sort(reverse=True)
print(arr[0]*arr[1]*arr[2])
