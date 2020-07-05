num = int(input())

ans = 0
seq = 1
arr = []
while num != 0:
    strnum = str(seq)
    length = strnum.__len__()
    lists = list(strnum)
    for i in range(length):
        arr.append(lists[i])
    num = num-length
    seq = seq+1

print(arr[arr.__len__()-1])