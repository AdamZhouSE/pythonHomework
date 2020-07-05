def func9():
    nums1 = list(map(int, input()[1:-1].split(",")))
    nums2 = list(map(int, input()[1:-1].split(",")))
    temp = [val for val in nums1 if val in nums2]
    print(sorted(temp))
    return
func9()