def wormhole_travel(val_arr, path_arr):
    res = []
    for i in range(len(val_arr)):
        tmp = [i]
        sum = val_arr[i]
        next = path_arr[i]
        while next != i+1:
            if next-1 not in tmp:
                tmp.append(next-1)
                sum += val_arr[next-1]
            else:
                break
            next = path_arr[next-1]
        res.append(sum)
    return res


if __name__ == '__main__':
    a = input()
    nums = input().split()
    path = input().split()
    for i in range(len(nums)):
        nums[i] = int(nums[i])
        path[i] = int(path[i])
    result = wormhole_travel(nums, path)
    for i in result:
        print(i)