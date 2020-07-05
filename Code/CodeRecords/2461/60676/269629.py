def find_rotate_element(arr):
    left = 0
    right = len(arr) - 1
    if arr[left] < arr[right]:
        return arr[0]
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            return arr[mid + 1]
        else:
            if arr[left] <= arr[mid]:
                left = mid + 1
            else:
                right = mid - 1


if __name__ == '__main__':
    print(find_rotate_element(eval(input())))