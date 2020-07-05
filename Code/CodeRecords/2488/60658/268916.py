arr = eval(input())
arr.sort(reverse = True)
arr[::2],arr[1::2]=arr[len(arr)//2:],arr[:len(arr)//2]
print(arr)