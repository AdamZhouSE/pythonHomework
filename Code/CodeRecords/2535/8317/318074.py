arr = input()
ret = start = 0
while start < len(arr):          #从头到尾遍历
    temp_end = arr[start]     #将当前的end设为数组中下标为start的值
    i = start
    while i <= temp_end:       #从start遍历到temp_end
        if arr[i] > temp_end :    #如果遍历过程中出现比temp_end更大值，就更新temp_end
            temp_end = arr[i]
        i += 1
    start = temp_end + 1
    ret += 1    #跳出循环，说明已经遍历到当前区间内最大值的下标的位置了，可以截断了，结果+1
print(ret)