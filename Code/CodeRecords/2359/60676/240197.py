def get_pairs(arr):
    if len(arr) < 3:
        return -1
    count = 0
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                ii = int(arr[i])
                jj = int(arr[j])
                kk = int(arr[k])
                if ii + jj == kk or ii + kk == jj or jj + kk == ii:
                    count += 1
    if count == 0:
        return -1
    return count


res = []
for i in range(int(input())):
    k = input()
    array = input().split()
    res.append(get_pairs(array))
for i in range(len(res)):
    print(res[i])