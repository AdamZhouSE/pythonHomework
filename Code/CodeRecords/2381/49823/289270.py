def dr(arr1,arr2):
    arr1 = arr1[::-1]
    arr2 = arr2[::-1]
    if len(arr1) > len(arr2):
        arr2 += [0] * (len(arr1) - len(arr2))
    elif len(arr1) < len(arr2):
        arr1 += [0] * (len(arr2) - len(arr1))
    arr1 += [0] * 4
    arr2 += [0] * 4
    arr = []
    for i in range(len(arr1)):
        arr.append(arr1[i] + arr2[i])
    ans = [0] * len(arr)
    for i in range(len(arr) - 2):
        ans[i] = arr[i] % 2
        count = arr[i] // 2
        arr[i + 1] = arr[i + 1] + count
        arr[i + 2] = arr[i + 2] + count
    for i in range(len(ans) - 1, -1, -1):
        if ans[i] == 0:
            ans.pop()
        else:
            break
    print(ans[::-1] if ans else [0])
if __name__ == '__main__':
    dr([int(i) for i in input().split(',')],[int(i) for i in input().split(',')])
