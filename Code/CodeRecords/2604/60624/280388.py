def func10():
    in_str = input()
    letters = []
    for i in in_str:
        if i.isalpha():
            letters.append(i)
    target = input()

    length = len(letters)
    low = 0
    high = length-1
    while low <= high:
        mid = (low+high) // 2
        if target < letters[mid]:
            high = mid-1
        else:
            low = mid+1
    print(letters[low%length])
    return
func10()
    