def reverse_pair(array):
    if len(array) < 3:
        return 0
    else:
        count = 0
        for i in range(len(array)-1):
            for j in range(i+1, len(array)):
                if int(array[i]) > 2 * int(array[j]):
                    count += 1
    return count


arr = input()[1:-1].split(',')
print(reverse_pair(arr))