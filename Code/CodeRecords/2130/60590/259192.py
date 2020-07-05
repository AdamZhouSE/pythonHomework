num = int(input())

ans = 0
seq = 1
arr = []
while num != 0 and num >0:
    strnum = str(seq)
    length = strnum.__len__()
    lists = list(strnum)
    if num < length:
        for i in range(num):
            arr.append(lists[i])
    else:
        for i in range(length):
            arr.append(lists[i])
    num = num-length
    seq = seq+1

#print(arr)
print(arr[arr.__len__()-1])