def h_index(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == len(arr) - mid:
            return arr[mid]
        elif arr[mid] < len(arr) - mid:
            left = mid + 1
        else:
            right = mid - 1
    if arr[left] <= len(arr) - left:
        return arr[left]
    return arr[left - 1]


if __name__ == '__main__':
    print(h_index(eval(input())))