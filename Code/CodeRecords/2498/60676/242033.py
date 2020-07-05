def odd_even_sort(array):
    ptr1 = 0
    ptr2 = len(array)-1
    while ptr1 < len(array):
        if ptr1 % 2 == array[ptr1] % 2:
            ptr1 += 1
        else:
            while ptr2 > ptr1:
                if ptr2 % 2 != array[ptr2] % 2 and array[ptr2] % 2 == ptr1 % 2:
                    temp = array[ptr2]
                    array[ptr2] = array[ptr1]
                    array[ptr1] = temp
                else:
                    ptr2 -= 1
            ptr2 = len(array)-1


arr = input()[1:-1].split(',')
for i in range(len(arr)):
    arr[i] = int(arr[i])
odd_even_sort(arr)
print(arr)