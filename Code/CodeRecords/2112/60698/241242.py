a = input()
arr = a.split(',')
arr = list(map(int, arr))
for i in range(0, len(arr)):
    if i not in arr:
        print(i)
        break
