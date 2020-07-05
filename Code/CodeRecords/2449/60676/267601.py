def find_rotate_index(arr):
    left = 0
    right = len(arr) - 1
    if arr[left] < arr[right]:
        return 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            return mid + 1
        else:
            if arr[left] <= arr[mid]:
                left = mid + 1
            else:
                right = mid - 1


def find_target_index(arr, num):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return 0 if arr[0] == num else -1
    left = 0
    right = len(arr) - 1
    r_i = find_rotate_index(arr)
    if arr[r_i] == num:
        return r_i
    if r_i != 0:
        if num > arr[-1]:
            right = r_i - 1
        else:
            left = r_i
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return mid
        elif num < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == '__main__':
    array = eval(input())
    print(find_target_index(array, int(input())))