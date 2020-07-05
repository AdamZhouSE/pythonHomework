arr1 = input()[1:-1].split(',')
arr2 = input()[1:-1].split(',')

ans = []
for num in arr1:
    if num in arr2:
        if not(int(num) in ans):
            ans.append(int(num))

ans = sorted(ans)
print(ans)