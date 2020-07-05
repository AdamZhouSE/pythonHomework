def compare_sort(arr1: list, arr2: list) -> list:
    count = []
    for i in arr2:
        j = 0
        while j < len(arr1):
            if i == arr1[j]:
                count.append(i)
                arr1.remove(i)
                j -= 1
            j += 1
    arr1.sort()
    count = count + arr1
    return count


l1 = eval(input())
l2 = eval(input())
print(compare_sort(l1, l2))