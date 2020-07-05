arr = eval(input())
lindex, rindex = 0, len(arr) - 1
while lindex < rindex:
    if arr[lindex] & 1 == 0:    #if a is even
        if arr[rindex] & 1 == 0:    #if b is even, too
            lindex += 1
        else:                       #if b is odd
            lindex += 1
            rindex -= 1
    else:                       #if a is odd
        if arr[rindex] & 1 == 0:    #if b is even
            temp = arr[lindex]
            arr[lindex] = arr[rindex]
            arr[rindex] = temp
            lindex += 1
            rindex -= 1
        else:                       #if b is odd, too
            rindex -= 1

print(arr[:])
