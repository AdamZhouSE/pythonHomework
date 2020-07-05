def steal_money(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return max(arr[0], arr[1])
    max_index = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[max_index]:
            max_index = i
    if max_index == 0:
        return arr[max_index] + steal_money(arr[max_index+2:])
    elif max_index == len(arr)-1:
        return arr[max_index] + steal_money(arr[:max_index-1])
    else:
        if arr[max_index-1] + arr[max_index+1] <= arr[max_index]:
            temp = arr[max_index]
            if max_index > 1:
                temp += steal_money(arr[:max_index-1])
            if max_index < len(arr)-2:
                temp += steal_money(arr[max_index+2:])
            return temp
        else:
            temp = arr[max_index-1] + arr[max_index+1]
            if max_index > 2:
                temp += steal_money(arr[:max_index-2])
            if max_index < len(arr)-3:
                temp += steal_money(arr[max_index+3:])
            return temp


result = []
for i in range(int(input())):
    a = input()
    array = input().split(' ')
    for j in range(len(array)):
        array[j] = int(array[j])
    result.append(steal_money(array))
for i in range(len(result)):
    print(result[i])