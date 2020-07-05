def arrays3(k,x,arr=[]):
    k = int(k)
    x = int(x)
    size = len(arr)
    left = 0
    right = size - 1
    remove_nums = size - k
    while remove_nums:
        if x - arr[left] <= arr[right] - x:
            right -= 1
        else:
            left += 1
        remove_nums -= 1
    list_re = []
    for i in range(left, right + 1):
        list_re.append(arr[i])
    print(list_re)
if __name__ == '__main__':
    list = eval(input())
    k = input()
    x = input()
    arrays3(k,x,list)