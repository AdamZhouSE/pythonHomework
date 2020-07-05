arr = input()
ret = start = 0
while start < len(arr):         
    temp_end = arr[start]   
    i = start
    while i <= temp_end:
        if arr[i] > temp_end :   
            temp_end = arr[i]
        i += 1
    start = temp_end + 1
    ret += 1   
print(ret)