def test():
    arr = eval(input())
    k = int(input())
    x = int(input())
    left = []
    same = []
    right = []
    result = []
    for i in range(0, len(arr)):
        if arr[i] < x:
            left.append(arr[i])
        elif arr[i] > x:
            right.append(arr[i])
        else:
            same.append(arr[i])
    result = result + same
    if len(result) >= k:
        result=sorted(result[0:k])
        return result
    else:
        index_l = len(left) - 1
        index_r = 0
        for i in range(0, k - len(result)):
            if 0 <= index_l and index_r < len(right):
                if x - left[index_l] <= right[index_r] - x:
                    result.append(left[index_l])
                    index_l = index_l - 1
                else:
                    result.append(right[index_r])
                    index_r = index_r + 1
            elif index_l < 0:
                result.append(right[index_r])
                index_r = index_r + 1
            elif index_r >= len(right):
                result.append(left[index_l])
                index_l = index_l - 1
        result=sorted(result)
        return result


if __name__ == '__main__':
    print(test())

