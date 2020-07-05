
def twoSum(numbers, target):

    """

    :type numbers: List[int]

    :type target: int

    :rtype: List[int]

    """

    n = len(numbers)

    for i in range(n - 1):

        for j in range(i + 1, n):

            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]

    return None




if __name__ == '__main__':
    alist = input().split(",")
    target = int(input())
    for i in range(len(alist)):
        alist[i] = int(alist[i])
    numIndex = twoSum(alist, target)
    print(numIndex)
