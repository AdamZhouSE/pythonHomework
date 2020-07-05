

def func(array) -> int :
    left , right , mid = 0 , len(array)-1, 0
    while right >= left :
        mid = int((right + left) / 2)
        if int(array[mid]) > int(array[right]) :
            left = mid + 1
        elif int(array[mid]) < int(array[left]) :
            rigth = mid
        else :
            right -= 1
    return array[left]


n = input().split(",")   #char array
print(func(n))