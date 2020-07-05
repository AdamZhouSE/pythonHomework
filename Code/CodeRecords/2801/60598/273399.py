length = int(input())
nums = list(map(int, input().split(" ")))


def clone(array):
    newList = list(array)
    return newList


def check(array):
    if array[0] + array[1] <= array[2]:
        return False
    elif array[0] + array[2] <= array[1]:
        return False
    elif array[2] + array[1] <= array[0]:
        return False
    else:
        return True


def trackBack(begin, array):
    N = len(array)
    if N == 3:
        if check(array):
            return True
        else:
            return False
    else:
        for i in range(begin, length):
            array.append(nums[i])
            temp = trackBack(i+1, clone(array))
            if temp:
                return True
            array.pop()
        return False


if trackBack(0, []):
    print("YES")
else:
    print("NO")
